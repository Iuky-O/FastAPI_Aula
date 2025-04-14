from pydantic import BaseModel

class Medico (BaseModel):
    nome: str
    idade: int