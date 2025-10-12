from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordRequestForm
from app.account.services import create_user, authenticate_user
from app.account.schema import UserCreate
from app.account.utilis import create_tokens, verify_refresh_token
from fastapi.responses import JSONResponse, Response

router = APIRouter(prefix="/account", tags=["Account"])


@router.post("/register")
async def register(user: UserCreate):
    return create_user(user)


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid Username or Password")
    tokens = create_tokens(user)
    response = JSONResponse(content={"access_token": tokens["access_token"]})
    response.set_cookie(
        "refresh_token",
        tokens["refresh_token"],
        httponly=True,
        secure=True,
        samesite="Lax",
        max_age=60 * 60 * 24 * 7,
    )
    return response


@router.post("/refresh")
def refresh(request: Request):
    token = request.cookies.get("refresh_token")
    if not token:
        raise HTTPException(status_code=401, detail="Missing refresh token")

    user = verify_refresh_token(token)
    return create_tokens(user, token)

@router.get("/me")
