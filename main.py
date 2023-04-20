from fastapi import FastAPI

from presentation import routers

app = FastAPI()
app.include_router(routers.router)
