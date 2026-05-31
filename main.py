import logging

from fastapi import FastAPI

from .routes import router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

app = FastAPI(
    title="MG Receipt OCR API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url=None,
)

app.include_router(router)
