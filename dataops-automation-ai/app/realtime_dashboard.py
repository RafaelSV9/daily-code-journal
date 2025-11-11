import streamlit as st
import requests
import os

API = os.getenv("DASHBOARD_API", "http://localhost:8000")
st.set_page_config(page_title="DataOps Dashboard", layout="wide")
st.title("📊 DataOps Automation + IA")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Cotações (últimas)")
    try:
        fx = requests.get(f"{API}/fx/latest?limit=15", timeout=10).json()
        st.table(fx)
    except Exception as e:
        st.error(f"Falha ao carregar cotações: {e}")

with col2:
    st.subheader("Atividade GitHub (recente)")
    try:
        gh = requests.get(f"{API}/github/activity?limit=20", timeout=10).json()
        st.table(gh)
    except Exception as e:
        st.error(f"Falha ao carregar GitHub: {e}")

st.subheader("Resumo IA")
try:
    ins = requests.get(f"{API}/insights", timeout=10).json()
    st.write(ins.get("insight") or "_Sem resumo ainda_")
except Exception as e:
    st.error(f"Falha ao carregar insight: {e}")
