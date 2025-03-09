import httpx
from freeapihub.config import API_URL


async def get_all_books():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}/api/v1/books")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"Error fetching books: {e}")
        return None


async def get_book_by_id(book_id: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_URL}/api/v1/books/{book_id}")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"Error fetching book {book_id}: {e}")
        return None
