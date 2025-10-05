from fastapi import APIRouter

router = APIRouter() #can add prefix by APIRouter(prefix="/users")

@router.get("/users")
async def get_all_users():
    return{"data" :"All users"}

@router.get("/users/me")
async def get_current_user():
    return {"data": "Current User"}

@router.get("/users/{user_id}")
async def get_single_user(user_id: int):
    return {"data": "Single User"}

@router.get("/products")
async def get_all_products():
    return {"data": "Products"}

@router.get("/products/{product_id}")
async def get_product_by_id(product_id):
    return {"data": "Single Product"}