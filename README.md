# resume-guard-rails

## Papel no ecossistema (PT)

Serviço de Segurança do Currículo Interativo. Valida inputs e outputs do fluxo de IA, evitando prompt
injections e alucinações antes que uma pergunta chegue ao `resume-llm-engine` ou que uma resposta chegue
ao usuário (ver Constitution Principle I, `.specify/memory/constitution.md`).

Fluxo de chamadas estrito (Constitution Principle II): `Frontend → bff → orchestrator → (guard-rails,
embeddings, llm-engine)`. Este serviço só deve ser chamado pelo `resume-orchestrator`.

## Status atual

Stub inicial (FastAPI "Hello World", `main.py`) — nenhuma lógica de validação/segurança foi implementada
ainda. A estrutura hexagonal completa (`applications/`, `domain/`, `infra/`, `config/`) descrita na
Constitution Principle II ainda não foi criada neste serviço.

## Stack

- Python + FastAPI

## Como rodar localmente

```sh
python -m venv .venv
.venv/Scripts/activate       # Windows
# source .venv/bin/activate  # Linux/Mac
pip install fastapi "uvicorn[standard]"
uvicorn main:app --reload
```

## Role in the ecosystem (EN)

The security service. Validates the AI flow's inputs and outputs, guarding against prompt injection and
hallucinations before a question reaches `resume-llm-engine` or an answer reaches the user. Currently a
stub — only the FastAPI "Hello World" endpoint exists.
