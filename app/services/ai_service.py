from transformers import pipeline

# Carregado uma única vez (IMPORTANTE para performance)
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

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


def confidence_level(score: float) -> str:
    if score >= 0.6:
        return "Alta"
    elif score >= 0.3:
        return "Média"
    return "Baixa"

def suggested_action(score: float) -> str:
    if score >= 0.6:
        return "Ação automática"
    elif score >= 0.3:
        return "Revisão rápida"
    return "Revisão humana"

def analyze_email(text: str) -> dict:
    classification = classifier(text, LABELS, multi_label=False)

    label = classification["labels"][0]
    confidence = float(classification["scores"][0])

    all_scores = {
        label: float(score)
        for label, score in zip(
            classification["labels"],
            classification["scores"]
        )
    }

    return {
        "category": label,
        "confidence": round(confidence, 4),
        "confidence_level": confidence_level(confidence),
        "productivity": "Produtivo" if label in PRODUCTIVE_LABELS else "Improdutivo",
        "suggested_action": suggested_action(confidence),
        "auto_reply": RESPONSE_TEMPLATES.get(label, "Obrigado pela mensagem."),
        "all_scores": all_scores
    }
