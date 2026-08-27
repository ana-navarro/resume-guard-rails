from fastapi import FastAPI

from applications.routes.guard_rails_routes import router as guard_rails_router

app = FastAPI()


@app.get("/")
def ler_raiz():
  return {"mensagem": "Olá, Mundo!"}


app.include_router(guard_rails_router)
