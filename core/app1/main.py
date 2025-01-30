from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello from App 1"}

@app.get("/call-app2")
async def call_app2():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://app2:8000/")
    return {"app2_response": response.json()}