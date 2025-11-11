    import time
    from typing import Dict, Any
    from ..storage import store
    from ..utils.config import settings

    def _has_openai():
        return bool(settings.openai_api_key)

    def summarize(metrics: Dict[str, Any]) -> str | None:
        """Gera um pequeno resumo com IA. Requer OPENAI_API_KEY.
        Você pode trocar o provedor facilmente; aqui fica um stub simplificado
        para evitar dependência dura no SDK.
        """
        if not _has_openai():
            return None
        # Implementação simples via API HTTP do OpenAI (sem SDK para evitar dependência extra)
        import requests, os
        headers = {
            "Authorization": f"Bearer {settings.openai_api_key}",
            "Content-Type": "application/json"
        }
        prompt = (
            "Resuma em 5 bullets o panorama atual (cotações e atividade GitHub). "
            "Foque em tendências e possíveis ações rápidas para o dia.
"
            f"Métricas: {metrics}"
        )
        body = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "Você é um analista DataOps objetivo."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.3
        }
        try:
            r = requests.post("https://api.openai.com/v1/chat/completions", json=body, headers=headers, timeout=30)
            r.raise_for_status()
            text = r.json()["choices"][0]["message"]["content"].strip()
            store.save_insight(text, int(time.time()))
            # também salva um arquivo markdown
            from pathlib import Path
            md = Path(__file__).resolve().parents[1] / "insights.md"
            md.write_text(text, encoding="utf-8")
            return text
        except Exception:
            return None
