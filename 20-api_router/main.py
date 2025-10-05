from fastapi import FastAPI
from routers import router 

app = FastAPI()

app.include_router(router, tags=["tag name"]) #"tag name " will be shown in swagger use to catgorize routes in swagger
# can add tags in routes and router = APIRouter(tags =  [""] separately
#can add multiple routes
#adding "prefix = "/user"" " inside app.include.router() will be consider "/user" as base url for all routes like "/create" will be treated as "/users/create" 