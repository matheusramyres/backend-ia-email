import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_API_TOKEN")


HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}


LABELS = [
    "Suporte",
    "Vendas",
    "Cobrança",
    "Parceria",
    "Reclamação",
    "Spam"
]

PRODUCTIVE_LABELS = {
    "Suporte",
    "Parceria",
    "Vendas",
    "Cobrança"
}

RESPONSE_TEMPLATES = {
    "Suporte": (
        "Olá! Recebemos sua solicitação de suporte e nossa equipe já está analisando. "
        "Em breve retornaremos com mais informações."
    ),
    "Reclamação": (
        "Olá! Lamentamos o ocorrido. Sua mensagem foi recebida e será analisada "
        "com atenção. Em breve entraremos em contato."
    ),
    "Parceria": (
        "Olá! Agradecemos seu contato e o interesse em parceria. "
        "Nossa equipe irá avaliar a proposta e retornaremos em breve."
    ),
    "Vendas": (
        "Olá! Obrigado pelo interesse em nossos produtos. "
        "Nossa equipe comercial entrará em contato em breve."
    ),
    "Cobrança": (
        "Olá! Recebemos sua mensagem sobre cobrança e iremos verificar as informações "
        "o mais rápido possível."
    ),
    "Spam": (
        "Obrigado pela mensagem."
    )
}


MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"
ROUTER_URL = "https://router.huggingface.co/v1/chat/completions"


def classify_email(text: str) -> dict:
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Você é um classificador de e-mails. "
                    f"Classifique o e-mail em UMA das categorias a seguir: {', '.join(LABELS)}. "
                    "Responda SOMENTE com o nome da categoria."
                )
            },
            {
                "role": "user",
                "content": text
            }
        ],
        "temperature": 0,
        "max_tokens": 10
    }



    response = requests.post(
        ROUTER_URL,
        headers=HEADERS,
        json=payload,
        timeout=30
    )

    if response.status_code != 200:
        print("❌ ERRO HF:", response.status_code, response.text)
        return None

    data = response.json()

    try:
        label = data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print("❌ RESPOSTA INVÁLIDA:", data)
        return None


    if label not in LABELS:
        label = "Spam"

    return {
        "label": label
    }

def generate_ai_reply(text: str) -> str | None:

    payload = {
        "model":MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "Você é um assistente que responde e-mails profissionais assumindo a identidade do usuário. Responda sempre em primeira pessoa do singular, como se fosse o próprio usuário escrevendo o e-mail. Use um tom educado, profissional, claro e natural, evitando linguagem robótica ou excessivamente formal. A resposta deve ser objetiva, cordial e adequada ao contexto do e-mail recebido. Gere apenas o texto final da resposta, sem explicações, comentários ou formatação extra."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }

    try:
        response = requests.post(
            ROUTER_URL,
            headers=HEADERS,
            json=payload,
            timeout=30
        )

        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"].strip()

    except Exception:
        return None

def analyze_email(text: str) -> dict:
    classification = classify_email(text)

    if not classification:
        return {
            "category": "Indefinido",
            "productivity": "Improdutivo",
            "auto_reply": "Não foi possível classificar o e-mail automaticamente.",
            "reply_source": "Fallback"
        }

    label = classification["label"]

    ai_reply = generate_ai_reply(text)

    return {
        "category": label,
        "productivity": (
            "Produtivo" if label in PRODUCTIVE_LABELS else "Improdutivo"
        ),
        "auto_reply": ai_reply or RESPONSE_TEMPLATES.get(label),
        "reply_source": "AI" if ai_reply else "Template"
    }
