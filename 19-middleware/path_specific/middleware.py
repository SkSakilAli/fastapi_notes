from fastapi import Request

#First Middleware
async def user_only(request: Request, call_next):
  if request.url.path.startswith("/users"):
    print("MiddleWare(1st) before processing the URL")
    print(f"Request{request.method}  {request.url}")

    response = await call_next(request) 

    print("Middleware(1st) after processing the request but before sending the response")
    print(f"Request Status Code {response.status_code}")
    return response
  else:
     response = await call_next(request)
     return response

#2nd middleware
#Creating middleware
async def product_only(request: Request, call_next):
 if request.url.path.startswith("/produts"):
    print("MiddleWare(2nd) before processing the URL")
    print(f"Request{request.method}  {request.url}")

    response = await call_next(request) 

    print("Middleware(2nd) after processing the request but before sending the response")
    print(f"Request Status Code {response.status_code}")
 else:
   response = await call_next(request)
   return response