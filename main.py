from fastapi import FastAPI

from bootstrap import get_container
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

# register ioc
app.state.ioc_container = get_container()

# register routes
app.include_router(loger_router)