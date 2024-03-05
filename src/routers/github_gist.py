from fastapi import APIRouter
from src.domain.github_client import github_client

router = APIRouter()

@router.get("/users/{id}")
async def get_gist(id: str):
    gists = github_client.get_user_gist(id)
    return gists