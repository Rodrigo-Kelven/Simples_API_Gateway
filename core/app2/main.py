from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello from App 2"}

@app.get("/call-app3")
async def call_app3():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://app3:8000/")
    return {"app3_response": response.json()}