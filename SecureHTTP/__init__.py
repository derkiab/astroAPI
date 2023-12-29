import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import azure.functions as func
import routers.satlocation as satlocation

app = FastAPI()

origins = [
    "http://localhost:3000",  # React app is served from localhost:3000
    "https://www.derquisanhueza.cl",  # Your React app's domain
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(satlocation.router, prefix="/satlocation")

def main(req: func.HttpRequest, context:func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req)

