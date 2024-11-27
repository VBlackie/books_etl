import os
from dotenv import load_dotenv
import requests
import logging

load_dotenv()

GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def validate_google_books_response(data):
    if not isinstance(data.get('items', []), list):
        logging.error("Invalid Google Books API response structure.")
        raise ValueError("Google Books API response is not in the expected format.")
    logging.info("Google Books API response validated successfully.")


def extract_books_from_google_books(query, max_results=10):
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&maxResults={max_results}&key={GOOGLE_BOOKS_API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses

        data = response.json()
        validate_google_books_response(data)  # Add validation here

        # Extract relevant fields
        books = []
        for book in data.get('items', []):
            volume_info = book.get('volumeInfo', {})
            books.append({
                'title': volume_info.get('title', 'Unknown Title'),
                'author': ', '.join(volume_info.get('authors', ['Unknown Author'])),
                'published_date': volume_info.get('publishedDate', 'Unknown Date'),
                'isbn': next(
                    (id['identifier'] for id in volume_info.get('industryIdentifiers', []) if id['type'] == 'ISBN_13'),
                    None),
                'source': 'Google Books'
            })

        logging.info(f"Successfully extracted {len(books)} books from Google Books API.")
        return books

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        raise
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error occurred: {req_err}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise


if __name__ == "__main__":
    # Test the function with a query like "data engineering"
    books = extract_books_from_google_books("data+engineering", max_results=10)
    print(books)
