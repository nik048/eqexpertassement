from fastapi import FastAPI
from src.routers import github_gist

app = FastAPI()

app.include_router(github_gist.router)