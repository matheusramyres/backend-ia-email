# 📧 Email AI Classifier – AutoU Challenge

Aplicação web que utiliza Inteligência Artificial para **classificar emails automaticamente** e **sugerir respostas adequadas**, reduzindo o trabalho manual de equipes que lidam com grande volume de mensagens.

Projeto desenvolvido como parte do **desafio técnico da AutoU**.

---

## 🛠️ Tecnologias Utilizadas

- **Python** — linguagem principal do projeto
- **FastAPI** — framework para construção da API REST
- **Uvicorn** — servidor ASGI para execução da aplicação FastAPI
- **python-multipart** — suporte a upload e processamento de arquivos (ex.: PDFs)
- **Requests** — consumo de APIs externas via HTTP
- **PyPDF2** — extração de texto a partir de arquivos PDF
- **NLTK** — pré-processamento e limpeza de texto para análise com IA

---

## 📦 Pré-requisitos

Antes de começar, você precisa ter instalado:

- **Python 3.10+**
- **Git**

---

## 🛡️ Configuração de Ambiente

- Variáveis de ambiente:
  - **HF_API_TOKEN** — Token da Hugging Face
  - **API_KEY** — Token interno, usado para autenticar as rotas
- Suporte a ambientes locais e produção:
  - .env carregado automaticamente fora do Render
  - Compatível com deploy em **Render, Netlify (frontend)** ou outros serviços

---

## 🧩 Variáveis de ambiente

Dentro do arquivo **.env.example** na raiz do projeto preenchas as variaveis ante antes de rodar o projeto.

```bash
API_KEY=chave_interna_da_api
HF_API_TOKEN=token_da_huggingface
```

- **API_KEY:** chave interna usada para autenticar as rotas da API (Bearer Token).
- **HF_API_TOKEN:** token de acesso à Hugging Face Inference API.

---

## 🔐 Autenticação

Todas as rotas da API são protegidas por autenticação via **Bearer Token**.

O token deve ser enviado no header:

```http
Authorization: Bearer API_KEY
```

Requisições sem token válido recebem resposta **401 Unauthorized**.

---

## 🔹 ▶️ Como rodar o projeto

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

---

## 🔹 Backend (Python + FastAPI)

O backend é responsável por analisar e-mails enviados como **texto ou arquivos PDF**, classificá-los, avaliar produtividade e gerar respostas automáticas, combinando regras de negócio com IA generativa.

### 🧠 API e Arquitetura

- **FastAPI** para criação da API REST

- Arquitetura desacoplada:
  - Regras de negócio independentes da IA
  - IA utilizada apenas para classificação e geração de respostas
- Integração externa via HTTP (`requests`)

### 🔄 Fluxo de Processamento

1. Recebe o e-mail (JSON ou PDF)
2. Extrai e normaliza o texto
3. Realiza pré-processamento com NLTK
4. Classifica o e-mail usando IA
5. Aplica regras de produtividade
6. Gera resposta automática via IA ou template
7. Retorna o resultado ao cliente

---

## 🤖 Inteligência Artificial (Hugging Face)

- **Plataforma:** Hugging Face Inference API
- **Modelo utilizado**:
  `meta-llama/Llama-3.1-8B-Instruct`

- **Endpoint oficial:**

```bash
  https://router.huggingface.co/v1/chat/completions
```

- **Autenticação:**
  Bearer Token via variável de ambiente (`HF_API_TOKEN`)

**Usos do modelo:**

- **Classificação de e-mails** em uma única categoria
- **Geração de respostas automáticas** em tom profissional
- Respostas sempre:
  - Em **primeira pessoa do singular**
  - Objetivas, educadas e naturais
  - Sem explicações extras ou formatação desnecessária

---

## 🏷️ Classificação de E-mails

Os e-mails são classificados automaticamente em uma das categorias abaixo:

- Suporte
- Vendas
- Cobrança
- Parceria
- Reclamação
- Spam
  Caso a IA retorne um valor inválido, o sistema aplica **fallback automático** para `Spam`.

---

## 📊 Avaliação de Produtividade

A produtividade é determinada **por regra de negócio**, não pela IA:

- **Produtivo:**
  - Suporte
  - Vendas
  - Cobrança
  - Parceria

- **Improdutivo:**
  - Reclamação
  - Spam

---

## ✉️ Respostas Automáticas

O sistema utiliza uma abordagem híbrida:

1. **IA Generativa**
   - Gera respostas personalizadas com o modelo LLaMA
   - Usada quando a chamada à IA é bem-sucedida

2. **Templates Pré-definidos (Fallback)**
   - Utilizados automaticamente caso a IA falhe
   - Templates específicos por categoria
   - Garantem resposta mesmo em caso de erro externo

---

## 🧪 Exemplo de Resposta da API

```json
{
  "category": "Vendas",
  "productivity": "Produtivo",
  "auto_reply": "Prezado(a) [Nome do destinatário],\n\nEstou escrevendo para agradecer pela oferta de compra do celular. Infelizmente, não estou interessado em adquirir um novo aparelho celular nesse momento. Obrigado novamente por entrar em contato.\n\nAtenciosamente,\n[Seu nome]",
  "reply_source": "AI"
}
```

---

## 🔌 Endpoints da API

### 📌 Analisar e-mail via JSON

**POST** `/api/analyze-email/json`

Analisa o conteúdo de um e-mail enviado como texto.

**Headers obrigatórios:**

```http
Authorization: Bearer API_KEY
Content-Type: application/json
```

**Body:**

```json
{
  "text": "Conteúdo do e-mail a ser analisado"
}
```

### 📌 Analisar e-mail via arquivo (PDF ou TXT)

**POST** /api/analyze-email/file

Analisa o conteúdo de um e-mail enviado como arquivo PDF ou TXT.

**Headers obrigatórios:**

```bash
Authorization: Bearer API_KEY
```

**Body (multipart/form-data):**

- `file`: arquivo PDF ou TXT contendo o e-mail

---

## 🔗 Link de produção

- Produção: [Link](https://backend-ia-email.onrender.com/)

---

## 🔗 Link do Front (produção e Github)

- **Produção:** [Link](https://email-ia.netlify.app/)
- **Github:** [Link](https://github.com/matheusramyres/email-ia-autou)

---

## 👨‍💻 Autor

### Matheus Ramyres da Silva Braz

Desenvolvedor Full Stack
