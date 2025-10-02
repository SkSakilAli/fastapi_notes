import services
from schema import create_user_request, create_post_request
from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

@app.put("/createuser")
async def createuser(data: create_user_request):
    services.create_a_user(data.name, data.email)
    return {"name": data.name,
            "email": data.email}
@app.post("/createpost")
async def createpost(data: create_post_request):
    services.create_a_post(data.title, data.content)
    return{
        "status": "Success",
        "Title": data.title
    }