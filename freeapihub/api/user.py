import httpx
from freeapihub.config import API_URL

async def get_all_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/api/v1/randomusers")
        return response.json()

async def get_user_by_id(user_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}/api/v1/randomusers/{user_id}")
        return response.json()
