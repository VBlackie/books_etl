import pytest
from unittest.mock import patch
from dags.extract import extract_books_data
from dags.extract_from_google_books import extract_books_from_google_books


def test_extract_books_data():
    mock_response = {
        'docs': [
            {
                'title': 'Test Book',
                'author_name': ['Test Author'],
                'first_publish_year': 2023,
                'isbn': ['1234567890']
            }
        ]
    }
    with patch('dags.extract.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        result = extract_books_data()
        expected_result = [{
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': 2023,
            'isbn': '1234567890',
            'source': 'OpenLibrary'
        }]

        assert result == expected_result


def test_extract_books_from_google_books():
    # Mock response for Google Books
    mock_response = {
        'items': [
            {
                'volumeInfo': {
                    'title': 'Google Book Test',
                    'authors': ['Google Author'],
                    'publishedDate': '2023',
                    'industryIdentifiers': [
                        {'type': 'ISBN_13', 'identifier': '9876543210'}
                    ]
                }
            }
        ]
    }

    with patch('dags.extract.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        # Test the function with a query and max_results
        result = extract_books_from_google_books(query="data+engineering", max_results=10)
        expected_result = [{
            'title': 'Google Book Test',
            'author': 'Google Author',
            'published_date': '2023',
            'isbn': '9876543210',
            'source': 'GoogleBooks'  # Include source for Google Books
        }]

        assert result == expected_result
