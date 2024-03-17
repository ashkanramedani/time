import os
import redis.asyncio as redis
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_limiter import FastAPILimiter
from sqlalchemy.exc import OperationalError

import db.models as models
from db.database import engine
from lib.log import logger
from router import routes

try:
    models.Base.metadata.create_all(bind=engine)
except OperationalError as e:
    logger.show_log(f"[ Could Not Create Engine ]: {e.__repr__()}", 'e')
    exit()

app = FastAPI()
WHITELISTED_IPS: List[str] = []
app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=['*'],
        allow_methods=["*"],
        allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    Redis_url = os.getenv('LOCAL_REDIS') if os.getenv('LOCAL_POSTGRES') else "redis://:eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81HBSDsdkjgasdj326@176.9.60.189:6379/0"
    await FastAPILimiter.init(redis=redis.from_url(Redis_url, encoding="utf8"))


@app.on_event("shutdown")
async def shutdown():
    await FastAPILimiter.close()


@app.get("/ping", tags=["Ping"])
def ping():
    return "Pong"


for route in routes:
    app.include_router(route)
