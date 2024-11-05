import requests


def extract_books_data():
    url = 'https://openlibrary.org/search.json?q=technology'  # Modify the query parameter as needed
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()['docs']
        # Extract and structure relevant fields
        extracted_data = [{
            'title': book.get('title', 'Unknown Title'),
            'author': ', '.join(book['author_name']) if 'author_name' in book else 'Unknown Author',
            'published_date': book.get('first_publish_year'),
            'isbn': book['isbn'][0] if 'isbn' in book else None
        } for book in data[:10]]  # Limiting to 10 records for simplicity
        return extracted_data
    else:
        raise Exception("Failed to fetch data from the API")
