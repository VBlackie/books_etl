import requests
import logging


def extract_books_data():
    url = 'https://openlibrary.org/search.json?q=data+engineering'  # Focused query on data engineering
    try:
        response = requests.get(url)
        response.raise_for_status()  # This raises an HTTPError for bad responses (e.g., 4xx, 5xx)

        data = response.json()['docs']

        # Extract relevant fields
        extracted_data = [{
            'title': book.get('title', 'Unknown Title'),
            'author': ', '.join(book['author_name']) if 'author_name' in book else 'Unknown Author',
            'published_date': book.get('first_publish_year'),
            'isbn': book['isbn'][0] if 'isbn' in book else None
        } for book in data]

        return extracted_data

    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
        raise
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error occurred: {req_err}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise
