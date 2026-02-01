# 📧 Email AI Classifier – AutoU Challenge

Aplicação web que utiliza Inteligência Artificial para **classificar emails automaticamente** e **sugerir respostas adequadas**, reduzindo o trabalho manual de equipes que lidam com grande volume de mensagens.

Projeto desenvolvido como parte do **desafio técnico da AutoU**.

---

## 🚀 Funcionalidades

- Upload de emails em formato `.txt` ou `.pdf`
- Inserção direta de texto do email
- Classificação automática do email em categorias:
  - Suporte
  - Reclamação
  - Parceria
  - Vendas
  - Cobrança
  - Spam
- Classificação final como:
  - **Produtivo**
  - **Improdutivo**
- Sugestão de resposta automática baseada na categoria
- Exibição do nível de confiança da IA

---

## 🧠 Arquitetura da Solução

### 🔹 Backend (Python + FastAPI)

- **FastAPI** para criação da API
- **Hugging Face Transformers**
  - Modelo: `facebook/bart-large-mnli`
  - Técnica: _Zero-Shot Classification_
- **NLTK** para pré-processamento de texto
- Regras de negócio separadas da IA (produtividade e respostas)

### 🔹 Frontend (Vite + React + Tailwind)

- Interface simples e intuitiva
- Upload de arquivos e exibição clara dos resultados
- Design focado em experiência do usuário

---

## 📊 Classificação de Produtividade

| Categoria  | Produtividade |
| ---------- | ------------- |
| Suporte    | Produtivo     |
| Reclamação | Improdutivo   |
| Parceria   | Produtivo     |
| Vendas     | Produtivo     |
| Cobrança   | Produtivo     |
| Spam       | Improdutivo   |

---

## 🧪 Exemplo de Resposta da API

```json
{
  "category": "Suporte",
  "confidence": 0.42,
  "confidence_level": "Média",
  "productivity": "Produtivo",
  "suggested_action": "Revisão rápida",
  "auto_reply": "Olá! Recebemos sua solicitação de suporte e nossa equipe já está analisando.",
  "all_scores": {
    "Suporte": 0.42,
    "Reclamação": 0.31,
    "Vendas": 0.12
  }
}
```

## ⚙️ Como rodar localmente

### 🔹 Pré-requisitos

- **Python 3.10+**
- **Node.js 22+**
- **Git**

### 🔹 Backend

```bash
cd backend-ia-email
python -m venv venv
source venv/bin/activate  #se for Windows execute assim: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API pode ser acessada localmente por esse link:

```bash
http://localhost:8000

```

## 📌 Observações Importantes

- A IA é utilizada exclusivamente para classificação dos emails

- As respostas automáticas seguem templates controlados, garantindo previsibilidade e segurança

- Em ambiente produtivo, os modelos de IA poderiam ser externalizados para APIs dedicadas

## 👨‍💻 Autor

### Matheus Ramyres da Silva Braz

Desenvolvedor Full Stack
