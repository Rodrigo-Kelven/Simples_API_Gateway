from fastapi import FastAPI, APIRouter

app = FastAPI(
    title="Um service teste",
    description="Um servico apenas para fins de testes",
)

@app.get(
    path="/home"
)
async def home():
    return {"message":"teste"}