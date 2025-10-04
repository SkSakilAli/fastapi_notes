from fastapi import FastAPI
from middleware import user_only, product_only

app= FastAPI()

app.middleware("http")(user_only)
app.middleware("http")(product_only)
#order matters here just like the previous one

@app.get("/users/{user_id}")
def function_one(user_id: int, sample_data: str):
    return{
        "user_id": user_id,
        "sample data": sample_data
    }
@app.post("/products")
def function_two(product_data: dict, product_id: int):
    return{
        "product data": product_data,
        "product_id": product_id
    }
