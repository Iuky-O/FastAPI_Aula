from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from http import HTTPStatus
from teste_poetry.schemas.schemas import Message

router = APIRouter()

@router.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá mundo!'}

@router.get('/teste_model', status_code=HTTPStatus.OK, response_model=Message)
def read_model():
    return {'message': 'Olá mundo!'}

@router.get('/teste_html', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_html():
    return """
        <html>
            <head>
                <title> Nosso olá mundo! </title>
            </head>
            <body>
                <h1> Olá mundo! </h1>
            </body>
        </html>
    """