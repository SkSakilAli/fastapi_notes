from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def products():
    return{
        "name":"Sk Sakil Ali",
        "age":21,
        "passion":"Nothing"
    }
##variable url
@app.get("/product/{product_id}")
async def product_one(product_id:int):
    return{
        "check":"this is working",
        "Product ID": product_id
    }
@app.post("product/new")
async def product_new(new_product: dict):
    return{
        "response": "Product Created",
        "new Product": new_product
    }
