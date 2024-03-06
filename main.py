from fastapi import FastAPI

from routes import loger_router

app = FastAPI(
    openapi_tags=[],
    title="Logger Application",
    description="",
    version="0.0.1",
    contact={
        "name": "Danushka Dissanayaka",
        "email": "dsjayamal@gmail.com",
    },)

# register routes
app.include_router(loger_router)