import token
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from services.user_services import UserService
from core.security import create_access_token, create_reflesh_token
from schemas.auth_schema import TokenSchema

auth_router = APIRouter()

@auth_router.post('/login',
                  summary='Cria o access token e o refresh token',
                  response_model=TokenSchema)
async  def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        email = data.username,
        password = data.password
    )
    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Email ou senha estão incorretos'
        )
    return {
        "access_token": create_access_token(usuario.user_id),
        "refresh_token": create_reflesh_token(usuario.user_id)
    }