🧾 README.md
# ⚙️ DataOps Automation + IA (Python)

Projeto prático desenvolvido por **Rafael dos Santos Vicente ([@RafaelSV9](https://github.com/RafaelSV9))** com foco em:
- **Integração de dados em tempo real**
- **Automação de tarefas**
- **Geração de insights com IA**

---

## 🚀 Funcionalidades

- 🔁 **Pipelines automáticos**:
  - Coleta de **cotações** (USD/BRL, EUR/BRL, BTC/BRL) via [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas)
  - Monitoramento de **atividade do GitHub** (issues, PRs, commits)
- 💾 Armazenamento local em **SQLite**
- 🌐 **API FastAPI** para fornecer dados atualizados
- 📊 **Dashboard Streamlit** em tempo real
- 🧠 Geração automática de **resumo inteligente** com **OpenAI GPT-4o mini**

---

## ⚙️ Como usar

### 1️⃣ Instale dependências
```bash
python -m venv .venv
source .venv/bin/activate  # (Linux/Mac)
.venv\Scripts\Activate.ps1 # (Windows PowerShell)
pip install -r requirements.txt

2️⃣ Configure variáveis de ambiente
cp .env.example .env
# Edite chaves e parâmetros se desejar

3️⃣ Execute a API e o agendador
python app/main.py

4️⃣ Abra o Dashboard
streamlit run app/realtime_dashboard.py


🌍 Endpoints disponíveis
EndpointDescrição/healthStatus do serviço/fx/latestÚltimas cotações de moedas/github/activityAtividades recentes do GitHub/insightsÚltimo resumo gerado por IA

🧩 Estrutura do Projeto
app/
  main.py                 # Orquestrador + agendador
  api.py                  # Rotas FastAPI
  pipelines/
    fx_rates.py           # Pipeline de cotações
    github_activity.py    # Pipeline de eventos do GitHub
  ai/
    summarizer.py         # IA para resumos
  storage/
    store.py              # Banco SQLite
  utils/
    config.py             # Carregamento de variáveis .env
  realtime_dashboard.py   # Dashboard Streamlit
scripts/
  run_all.sh              # Atalho para execução


🧠 Insight da IA (exemplo)
• Dólar e Bitcoin subiram nas últimas horas.
• Atividade intensa no repositório daily-commit-lab.
• Nenhum erro crítico nos pipelines.
• Próximos passos: revisar endpoints e testar webhooks.


🧑‍💻 Autor
Rafael dos Santos Vicente
📍 Londrina - PR
💼 Telecom Engineer & Software Developer
🔗 GitHub: @RafaelSV9

🇬🇧 English Summary
DataOps Automation + AI (Python) — practical project by RafaelSV9 integrating data pipelines, task automation, and AI insights.
Features:


Real-time data collection (FX rates, GitHub events)


SQLite storage


FastAPI backend + Streamlit dashboard


Optional OpenAI GPT-4o summaries


Ideal for daily commits and continuous portfolio growth 🚀

---

## 💬 **Commit Message sugerido**

```bash
git add .
git commit -m "feat: projeto DataOps Automation + IA (integração de dados + insights com Python)"
git push origin main


