from fastapi import Request

#First Middleware
async def first_middleware(request: Request, call_next):
    print("MiddleWare(1st) before processing the URL")
    print(f"Request{request.method}  {request.url}")

    response = await call_next(request) 

    print("Middleware(1st) after processing the request but before sending the response")
    print(f"Request Status Code {response.status_code}")
    return response

#2nd middleware
#Creating middleware
async def second_middleware(request: Request, call_next):
    print("MiddleWare(2nd) before processing the URL")
    print(f"Request{request.method}  {request.url}")

    response = await call_next(request) 

    print("Middleware(2nd) after processing the request but before sending the response")
    print(f"Request Status Code {response.status_code}")
