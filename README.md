# LLM-OKF

LLM-OKF is a small FastAPI and vanilla JavaScript application for asking
questions about Large Language Model concepts. It uses Markdown files as a
structured Open Knowledge Format (OKF) knowledge base, retrieves relevant
concepts and related concepts, and sends the resulting context to a Groq-hosted
language model.

## Features

- YAML frontmatter and relationship links in Markdown knowledge files
- Token-overlap retrieval weighted by title, tags, description, and content
- Depth-limited traversal of related concepts for richer answer context
- Groq-powered grounded answers
- Knowledge graph endpoint with nodes and edges
- Browser UI with:
  - API key controls in the left sidebar
  - Concepts used for the current answer in the left sidebar
  - Bottom agent composer
  - Light-blue visual theme
  - Rendering for headings, bold text, italic text, inline code, and lists

## Project Structure

```text
llm-okf/
├── app/
│   ├── main.py                 # FastAPI application
│   ├── routes/
│   │   ├── knowledge.py        # Knowledge graph endpoint
│   │   └── query.py            # Question-answering endpoint
│   ├── services/
│   │   ├── groq_service.py     # Groq answer generation
│   │   ├── retriever.py        # Relevance scoring and graph expansion
│   │   ├── test_groq.py        # Groq integration test
│   │   └── test_retriever.py   # Retriever test
│   └── okf/
│       ├── loader.py           # Markdown and YAML loader
│       └── test_loader.py      # Loader test
├── knowledge/
│   ├── index.md
│   └── concepts/               # LLM concept documents
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
├── .env                        # Local configuration; do not commit
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

From the project root on Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Create or update `.env` with a Groq key and a model available to your account:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=openai/gpt-oss-20b
```

Do not commit `.env` or expose the API key in source control.

## Run the API

Start the FastAPI server from the project root:

```powershell
uvicorn app.main:app --reload
```

The API is available at `http://127.0.0.1:8000`.

The web interface is served at the same address:

- Local app: `http://127.0.0.1:8000/`
- Deployed app: [https://llm-okf.vercel.app/](https://llm-okf.vercel.app/)

Interactive API documentation is available at:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/redoc`

## Deploy to Vercel

The Vercel serverless entrypoint is `api/index.py`, which exposes the FastAPI
application as `app`. Deploy from the project root with the Vercel CLI or by
connecting the repository in the Vercel dashboard.

Add these environment variables in the Vercel project settings for the
Production, Preview, or Development environments that you use:

```text
GROQ_API_KEY
GROQ_MODEL
```

The current working model is `openai/gpt-oss-20b`, but model availability is
account-dependent. Do not rely on the local `.env` file in a Vercel deployment;
Vercel does not receive that ignored file automatically.

The frontend uses the same origin in a deployed environment. Locally it uses
`http://127.0.0.1:8000`.

## API Endpoints

### Health check

```http
GET /health
```

### Ask a question

```http
POST /api/ask
Content-Type: application/json
```

Request body:

```json
{
  "question": "What is the relationship between LoRA and QLoRA?"
}
```

The response includes the generated answer and the concepts used to build the
answer context. Relationship traversal data is also returned by the API for
programmatic use, although the frontend displays only the concepts used.

### Knowledge graph

```http
GET /api/knowledge/graph
```

Returns the loaded concept nodes and valid relationship edges.

## Knowledge Documents

Concept files live in `knowledge/concepts/`. A document can use YAML
frontmatter like this:

```markdown
---
type: concept
id: lora
title: LoRA
description: A parameter-efficient fine-tuning method.
tags:
  - lora
  - peft
---

# LoRA

LoRA adapts a pretrained model using small trainable matrices.

## Relationships

- part_of: [[parameter-efficient-fine-tuning]]
- related_to: [[qlora]]
```

The loader reads Markdown files, parses frontmatter, extracts `[[concept-id]]`
relationships, and resolves the knowledge directory relative to the project
rather than the current shell directory.

## Retrieval Flow

1. The question is tokenized into normalized terms.
2. Concepts are scored using title, tag, description, and content matches.
3. The highest-scoring concepts are selected.
4. Related concepts are traversed to a limited depth.
5. The retrieved documents are assembled into model context.
6. Groq generates a grounded answer from that context.

## Run the Checks

The test scripts can be run directly from the project root:

```powershell
& .\.venv\Scripts\python.exe .\app\okf\test_loader.py
& .\.venv\Scripts\python.exe .\app\services\test_retriever.py
& .\.venv\Scripts\python.exe .\app\services\test_groq.py
```

The Groq test makes a live API request. The loader and retriever tests do not
require a model request.

## Frontend

With the API running, open `http://127.0.0.1:8000/`. FastAPI serves
`frontend/index.html`, `frontend/style.css`, and `frontend/script.js` from the
same origin, so the page and API work together without opening the HTML file
directly.

The interface sends questions to `/api/ask`, shows the generated answer, and
updates the sidebar with the concepts returned by the API. It does not display
the internal knowledge traversal.
