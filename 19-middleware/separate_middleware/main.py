from fastapi import FastAPI
from middleware import first_middleware, second_middleware

app= FastAPI()

app.middleware("http")(first_middleware)
app.middleware("http")(second_middleware)
#order matters here just like the previous one