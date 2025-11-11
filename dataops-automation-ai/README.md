# DataOps Automation + IA (Python)

Projeto prático para **integração de dados**, **automação de tarefas** e **insights com IA**.

**Recursos:**
- Pipelines periódicos:
  - **Cotações** (AwesomeAPI) para pares: `USD/BRL`, `EUR/BRL`, `BTC/BRL` (configurável).
  - **GitHub Watch**: issues/commits recentes de repositórios públicos.
- Armazenamento em **SQLite** (local, sem complicação).
- **API FastAPI** para servir dados em tempo real.
- **Dashboard Streamlit** simples para visualização.
- **Resumo com IA** (OpenAI) gerando `insights.md` automaticamente, opcional.

## Como rodar
```bash
# 1) Clonar/copiar este projeto
# 2) Criar e ativar venv
python -m venv .venv && source .venv/bin/activate  # (Linux/Mac)
# No Windows (PowerShell):  .venv\Scripts\Activate.ps1

# 3) Instalar dependências
pip install -r requirements.txt

# 4) Configurar variáveis
cp .env.example .env
# edite .env e informe OPENAI_API_KEY (opcional) e ajustes de agenda

# 5) Iniciar as rotinas
# API (dados em tempo real) + agendador
python app/main.py

# 6) Dashboard (em outro terminal)
streamlit run app/realtime_dashboard.py
```

## Endpoints úteis
- `GET /health`
- `GET /fx/latest` — últimas cotações
- `GET /github/activity` — atividade recente
- `GET /insights` — último resumo da IA (se habilitado)

## Estrutura
```text
app/
  main.py                 # orquestrador + API
  api.py                  # rotas FastAPI
  pipelines/
    fx_rates.py           # AwesomeAPI (cotações)
    github_activity.py    # Issues/commits recentes
  ai/
    summarizer.py         # resumo com OpenAI
  storage/
    store.py              # SQLite + helpers
  utils/
    config.py             # .env loader e helpers
  realtime_dashboard.py   # Streamlit
scripts/
  run_all.sh              # atalho local
```

## Observações
- O projeto usa **APScheduler** com CRON da `.env` (ex.: `*/5 * * * *` = a cada 5 min).
- Sem chave OpenAI, tudo roda **menos** a geração de `insights.md`.
- Para ambientes com firewall, ajuste endpoints das APIs públicas.

---
Feito para manter o **commit diário** do RafaelSV9 com algo útil e escalável.
