# resume-guard-rails

## Papel no ecossistema (PT)

Serviço de Segurança do Currículo Interativo. Valida inputs e outputs do fluxo de IA, evitando prompt
injections e alucinações antes que uma pergunta chegue ao `resume-llm-engine` ou que uma resposta chegue
ao usuário (ver Constitution Principle I, `.specify/memory/constitution.md`).

Fluxo de chamadas estrito (Constitution Principle II): `Frontend → bff → orchestrator → (guard-rails,
embeddings, llm-engine)`. Este serviço só deve ser chamado pelo `resume-orchestrator`.

## Status atual

Primeira feature real: dois validadores expostos via HTTP (Constitution Principle I — "valida inputs e
outputs, evitando prompt injections e alucinações"):

- **`POST /validate-input`**: bloqueia perguntas maliciosas (blocklist) ou fora do escopo de
  carreira/currículo (scope keywords) **antes** de a pergunta chegar ao `resume-llm-engine`.
- **`POST /validate-output`**: sinaliza afirmações específicas na resposta gerada (nomes próprios,
  números com unidade) que não estão fundamentadas no contexto-fonte fornecido — um indício heurístico
  de possível alucinação.

**Limitação importante e deliberada**: como nenhum provedor de IA/LLM/embeddings está configurado
ainda neste projeto, os dois validadores são **heurísticas determinísticas baseadas em regras**
(substring matching / regex), não classificação por IA. Espere falsos positivos/negativos — isso é uma
primeira linha de defesa, não uma solução robusta de produção.

**Fora de escopo desta feature** (task futura): fiação real com `resume-orchestrator` (que deveria
chamar estes endpoints antes/depois de chamar `resume-llm-engine`) e qualquer integração com
`resume-embeddings`/modelo de IA.

## Stack

- Python + FastAPI
- `pytest` + `pytest-cov` (testes, cobertura mínima de 80% — Constitution Principle III)
- `ruff` (lint)

## Como rodar localmente

```sh
python -m venv .venv
.venv/Scripts/activate       # Windows
# source .venv/bin/activate  # Linux/Mac
pip install -r requirements-dev.txt
uvicorn main:app --reload
```

## Rodando a pipeline local (lint + testes + cobertura)

```sh
make validate-pipeline
```

Em ambientes sem `make` (ex.: Git Bash no Windows), rode os passos equivalentes diretamente:

```sh
python -m ruff check .
python scripts/gen_coveragerc.py
python -m pytest --cov --cov-config=.coveragerc --cov-report=term-missing
```

## Role in the ecosystem (EN)

The security service. Validates the AI flow's inputs and outputs, guarding against prompt injection and
hallucinations before a question reaches `resume-llm-engine` or an answer reaches the user. First real
feature: `POST /validate-input` (blocklist + scope-keyword check) and `POST /validate-output`
(heuristic groundedness check against a provided source context). Both are deterministic, rule-based
heuristics — no AI/LLM provider is configured anywhere in this project yet, so this is a first line of
defense, not production-grade moderation or fact-checking. Wiring `resume-orchestrator` to actually
call these endpoints is out of scope for now.
