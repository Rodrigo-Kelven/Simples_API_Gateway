from fastapi import FastAPI
from controller.routs_items import app

app = FastAPI()

app.include_router(app)
