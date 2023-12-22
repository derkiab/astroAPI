import logging
from fastapi import FastAPI
import azure.functions as func
import routers.satlocation as satlocation

app = FastAPI()
app.include_router(satlocation.router, prefix="/satlocation")

def main(req: func.HttpRequest, context:func.Context) -> func.HttpResponse:
    return func.AsgiMiddleware(app).handle(req)

