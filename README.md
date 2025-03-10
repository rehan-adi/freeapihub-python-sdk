# FreeApiHub SDK (Python)

A Python SDK for **FreeApiHub**, providing simple access to free APIs with support for data retrieval and integration. Ideal for Python projects needing quick API access.

## Features

- **Simple API calls** to interact with different endpoints (e.g., books, jokes, quotes).
- **Lightweight and efficient** implementation using `httpx`.
- **Simple integration** into your Python projects.

### 🚀 Docs  
FreeApiHub API Documentation: [FreeApiHub Docs](https://freeapi-hub.vercel.app/docs)  

### Requirements

- Python 3.7+
- `httpx` (installed automatically with `pip install freeapihub`)


## Installation

Install the SDK using pip:

### Using pip

```bash
pip install freeapihub
```

## Usage

### Import the SDK

In a Python file, import the necessary functions.

```python
from freeapihub import get_all_books, get_book_by_id
```

### Example 1: Fetching all books

```python
import asyncio
from freeapihub import get_all_books

async def fetch_books():
    try:
        books = await get_all_books()
        print(books)
    except Exception as e:
        print(f"Error fetching books: {e}")

asyncio.run(fetch_books())

```

### Example 2: Fetch a Book by ID

```python
import asyncio
from freeapihub import get_book_by_id

async def fetch_book(book_id: str):
    try:
        book = await get_book_by_id(book_id)
        print(book)
    except Exception as e:
        print(f"Error fetching book with ID {book_id}: {e}")

asyncio.run(fetch_book("book-id-here"))
```

### Available Methods

- `get_all_jokes()`: Fetches all jokes from the API.
- `get_joke_by_id(joke_id: str)`: Fetches a joke by its ID.
- `get_all_books()`: Fetches all books from the API.
- `get_book_by_id(book_id: str)`: Fetches a book by its ID.
- `get_all_users()`: Fetches all users from the API.
- `get_user_by_id(user_id: str)`: Fetches a user by their ID.
- `get_all_stocks()`: Fetches all stock data.
- `get_stock_by_id(stock_id: str)`: Fetches stock data by its ID.
- `get_all_quotes()`: Fetches all quotes.
- `get_quote_by_id(quote_id: str)`: Fetches a quote by its ID.
- `get_all_products()`: Fetches all products.
- `get_product_by_id(product_id: str)`: Fetches a product by its ID.
- `get_all_programming_languages()`: Fetches all programming languages.
- `get_programming_language_by_id(language_id: str)`: Fetches a programming language by its ID.

## API Documentation

For detailed documentation on each API endpoint, refer to the FreeApiHub API documentation.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests on GitHub.


### Author

Created by [Rehan](https://github.com/rehan-adi)
