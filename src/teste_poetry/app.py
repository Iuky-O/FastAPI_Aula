from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from http import HTTPStatus
from teste_poetry.schemas.schemas import Message
from teste_poetry.api.router import testesRouter, userRouter, medicoRouter

app = FastAPI()

app.include_router(userRouter.router, prefix="/user", tags=["Usuários"])
app.include_router(testesRouter.router, prefix="/testes", tags=["Testes"])
app.include_router(medicoRouter.router, prefix="/medicos", tags=["Medicos"])




