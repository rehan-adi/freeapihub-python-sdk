import httpx
from freeapihub.config import API_URL


async def get_all_users():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}/api/v1/randomusers")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"Failed to fetch users: {e}")
        return None


async def get_user_by_id(user_id: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}/api/v1/randomusers/{user_id}")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"Failed to fetch user with ID {user_id}: {e}")
        return None
