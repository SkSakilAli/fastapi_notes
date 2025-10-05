from fastapi import FastAPI, Depends
from typing import Annotated


app = FastAPI()

#Creating Dependency Function
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {
  "q" : q,
  "skip": skip,
  "limit": limit
    }

# Using Dependency in Endpoints
@app.get("/items")
async def read_items(commons : Annotated[dict, Depends(common_parameters)]): 
    return commons
