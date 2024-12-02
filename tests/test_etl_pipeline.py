import pytest
from unittest.mock import patch, MagicMock
from dags.extract import extract_books_data
from dags.extract_from_google_books import extract_books_from_google_books
from dags.transform import transform_books_data
from dags.load import load_books_data
import logging

logging.basicConfig(level=logging.DEBUG)


def normalize_query(query):
    """Normalize SQL query by removing extra spaces, newlines, and converting to lowercase."""
    return " ".join(query.strip().lower().split())


def test_etl_pipeline_integration():
    # Step 1: Mock API responses for both sources
    mock_openlibrary_response = {
        'docs': [
            {
                'title': 'Test Book',
                'author_name': ['Test Author'],
                'first_publish_year': 2023,
                'isbn': ['1234567890']
            }
        ]
    }

    mock_google_books_response = {
        'items': [
            {
                'volumeInfo': {
                    'title': 'Test Book 2',
                    'authors': ['Author 2'],
                    'publishedDate': '2022',
                    'industryIdentifiers': [{'type': 'ISBN_13', 'identifier': '0987654321'}]
                }
            }
        ]
    }

    # Mock database engine and connection
    with patch('dags.load.create_engine') as mock_create_engine, \
            patch('dags.extract.requests.get') as mock_get_openlibrary, \
            patch('dags.extract_from_google_books.requests.get') as mock_get_google_books:

        # Mock the API requests
        mock_get_openlibrary.return_value.status_code = 200
        mock_get_openlibrary.return_value.json.return_value = mock_openlibrary_response

        mock_get_google_books.return_value.status_code = 200
        mock_get_google_books.return_value.json.return_value = mock_google_books_response

        # Mock the database connection
        mock_engine = MagicMock()
        mock_connection = mock_engine.connect.return_value.__enter__.return_value
        mock_create_engine.return_value = mock_engine

        def mock_execute(query, *args, **kwargs):
            query = query.strip().lower()
            if "select count(*) from books" in query:
                return MagicMock(scalar=lambda: 1)  # Simulate book count
            elif "create table" in query or "insert into" in query:
                return None  # Simulate table creation and inserts
            elif "select isbn, count(*) from books" in query:
                return MagicMock(fetchall=lambda: [])  # No duplicates
            else:
                raise ValueError(f"Unexpected query: {query}")

        mock_connection.execute.side_effect = mock_execute

        # Step 2: Run the extract step for OpenLibrary
        # mock_get_openlibrary.return_value.json.return_value = mock_openlibrary_response
        # print("Mocked OpenLibrary Response:", mock_get_openlibrary.return_value.json.return_value)
        logging.debug("Mocked OpenLibrary Response: %s", mock_get_openlibrary.return_value.json.return_value)
        extracted_openlibrary_data = extract_books_data()
        assert len(extracted_openlibrary_data) == 1

        # Step 3: Run the extract step for Google Books
        extracted_google_books_data = extract_books_from_google_books("data+engineering", max_results=1)
        assert len(extracted_google_books_data) == 1

        # Step 4: Transform both datasets
        transformed_openlibrary_data = transform_books_data(extracted_openlibrary_data)
        transformed_google_books_data = transform_books_data(extracted_google_books_data)

        assert len(transformed_openlibrary_data) == 1
        assert len(transformed_google_books_data) == 1

        # Step 5: Load both datasets
        load_books_data(transformed_openlibrary_data)
        load_books_data(transformed_google_books_data)

        # Debugging executed queries
        executed_queries = [normalize_query(call[0][0]) for call in mock_connection.execute.call_args_list]
        print("\nNormalized Executed Queries:")
        for query in executed_queries:
            print(query)

        # Assert that table creation queries are present
        expected_books_table_query = normalize_query("""
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                published_date INT,
                isbn VARCHAR(20) UNIQUE,
                source VARCHAR(50)
            );
        """)
        assert expected_books_table_query in executed_queries, "Books table creation query not executed."
