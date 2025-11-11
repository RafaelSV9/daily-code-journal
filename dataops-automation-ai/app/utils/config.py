import os
from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List

load_dotenv()

class Settings(BaseModel):
    project_name: str = os.getenv("PROJECT_NAME", "DataOps Automation AI")
    owner_name: str = os.getenv("OWNER_NAME", "Rafael SV")
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8000"))

    fx_pairs: List[str] = [x.strip() for x in os.getenv("FX_PAIRS", "USD-BRL,BTC-BRL").split(",") if x.strip()]
    schedule_fx: str = os.getenv("SCHEDULE_FX", "*/5 * * * *")
    schedule_github: str = os.getenv("SCHEDULE_GITHUB", "*/10 * * * *")

    github_watch_repos: List[str] = [x.strip() for x in os.getenv("GITHUB_WATCH_REPOS", "").split(",") if x.strip()]
    github_token: str | None = os.getenv("GITHUB_TOKEN")

    openai_api_key: str | None = os.getenv("OPENAI_API_KEY")

    repo_owner: str = os.getenv("REPO_OWNER", "RafaelSV9")
    repo_name: str = os.getenv("REPO_NAME", "daily-commit-lab")

settings = Settings()
