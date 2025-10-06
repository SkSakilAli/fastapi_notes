from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", staticFiles(directory = "/static"), name="static) 
#app.mount("/rul", staticFiles(directory = "directory_location",  name = "unique_name/identifier")
