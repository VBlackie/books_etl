import requests


def extract_books_data():
    query_terms = ["data science", "data engineering", "artificial intelligence", "machine learning", "big data"]
    extracted_data = []

    for term in query_terms:
        url = f'https://openlibrary.org/search.json?q={term}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json().get('docs', [])
            # Extract and structure relevant fields for each book
            term_data = [{
                'title': book.get('title', 'Unknown Title'),
                'author': ', '.join(book['author_name']) if 'author_name' in book else 'Unknown Author',
                'published_date': book.get('first_publish_year'),
                'isbn': book['isbn'][0] if 'isbn' in book else None
            } for book in data[:10]]  # Limiting to 10 records per term for simplicity

            extracted_data.extend(term_data)
        else:
            print(f"Failed to fetch data for term '{term}'")

    return extracted_data
