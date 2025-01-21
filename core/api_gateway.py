from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI()

# URLs dos serviços que o API Gateway irá encaminhar as requisições
SERVICE_A_URL = "http://localhost:8001"
SERVICE_B_URL = "http://localhost:8002"

@app.get("/service-a/{item_id}")
async def get_service_a(item_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{SERVICE_A_URL}/items/{item_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()

@app.get("/service-b/{item_id}")
async def get_service_b(item_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{SERVICE_B_URL}/items/{item_id}")
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)
        return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
