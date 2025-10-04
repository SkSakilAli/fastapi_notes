from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
app = FastAPI()

app.add.middleware(HTTPSRedirectMiddleware) #Redricts http request to https
app.add.middleware(TrustedHostMiddleware, allowed_hosts = ["localhost", "127.0.0.1"])