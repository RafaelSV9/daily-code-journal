import asyncio
import uvicorn
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from .pipelines.fx_rates import run_fx_pipeline
from .pipelines.github_activity import run_github_pipeline
from .ai.summarizer import summarize
from .storage import store
from .utils.config import settings

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("dataops")

def schedule_jobs(sched: AsyncIOScheduler):
    # FX
    fx_trigger = CronTrigger.from_crontab(settings.schedule_fx)
    sched.add_job(lambda: run_fx_pipeline(settings.fx_pairs), fx_trigger, name="fx")
    # Github
    gh_trigger = CronTrigger.from_crontab(settings.schedule_github)
    sched.add_job(lambda: run_github_pipeline(settings.github_watch_repos), gh_trigger, name="github")
    # Insights (após FX e GH): roda 1x/hora
    sched.add_job(generate_insights_job, CronTrigger.from_crontab("0 * * * *"), name="insights")

def generate_insights_job():
    try:
        fx = store.latest_fx(limit=10)
        gh = store.latest_github(limit=20)
        metrics = {
            "fx": [{"pair": p, "bid": b, "ask": a, "ts": ts} for (p,b,a,ts) in fx],
            "github": [{"repo": r, "type": t, "title": ttl} for (r,t,ttl,_,_) in gh]
        }
        summarize(metrics)
        log.info("Insights atualizados")
    except Exception as e:
        log.exception("Erro ao gerar insights: %s", e)

async def run():
    store.init_db()
    sched = AsyncIOScheduler()
    schedule_jobs(sched)
    sched.start()
    log.info("Agendador iniciado")
    config = uvicorn.Config("app.api:app", host=settings.api_host, port=settings.api_port, reload=False)
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(run())
