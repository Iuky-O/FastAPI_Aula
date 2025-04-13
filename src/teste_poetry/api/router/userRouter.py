from http import HTTPStatus
from fastapi import APIRouter
from teste_poetry.schemas.user import User, UserPublic, \
                                    UserDB, UserPublicDB, UserList

router = APIRouter()

database = []

@router.post('/create_user', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: User):
    return user



@router.post('/create_user_db', status_code=HTTPStatus.CREATED, response_model=UserPublicDB)
def create_user_db(user: User):

    user_data = UserDB(**user.model_dump(), id = len(database)+1)
    
    database.append(user_data)

    return user_data

@router.get('/get_user_db', response_model=UserList)
def get_users_db():
    return {'users': database}