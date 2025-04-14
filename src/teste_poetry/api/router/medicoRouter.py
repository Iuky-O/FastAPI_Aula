from http import HTTPStatus
from fastapi import APIRouter
from teste_poetry.schemas.medicos import Medico

router = APIRouter()

medico = {'nome': 'teste', 'idade': 20}

@router.get('/medico')
def get_medicos():
    return medico

@router.post('/medico')
def post_medico(med: Medico):
    return med

