import pytest
from unittest.mock import patch, MagicMock
from dags.extract import extract_books_data
from dags.transform import transform_books_data
from dags.load import load_books_data


def normalize_query(query):
    """Normalize SQL query by removing extra spaces, newlines, and converting to lowercase."""
    return " ".join(query.strip().lower().split())


def test_etl_pipeline_integration():
    # Step 1: Mock API response for extract step
    mock_api_response = {
        'docs': [
            {
                'title': 'Test Book 1',
                'author_name': ['Author 1'],
                'first_publish_year': 2023,
                'isbn': ['1234567890']
            },
            {
                'title': 'Test Book 2',
                'author_name': ['Author 2'],
                'first_publish_year': 2022,
                'isbn': ['0987654321']
            }
        ]
    }

    # Mock database engine and connection
    with patch('dags.load.create_engine') as mock_create_engine, \
            patch('dags.extract.requests.get') as mock_get:

        # Mock the API request
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_api_response

        # Mock the database connection
        mock_engine = MagicMock()
        mock_connection = mock_engine.connect.return_value.__enter__.return_value
        mock_create_engine.return_value = mock_engine

        # Set up mocked responses for `execute` calls
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

        # Step 2: Run the extract step
        extracted_data = extract_books_data()
        assert len(extracted_data) == 2  # Ensure we extracted two books

        # Step 3: Run the transform step
        transformed_data = transform_books_data(extracted_data)
        assert len(transformed_data) == 2  # Ensure transformation was successful

        # Step 4: Run the load step
        load_books_data(transformed_data)

        # Debugging executed queries
        executed_queries = [normalize_query(call[0][0]) for call in mock_connection.execute.call_args_list]
        print("\nNormalized Executed Queries:")
        for query in executed_queries:
            print(query)

        # Normalize expected queries
        expected_query = normalize_query("""
            CREATE TABLE IF NOT EXISTS books (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255),
                author VARCHAR(255),
                published_date INT,
                isbn VARCHAR(20) UNIQUE
            );
        """)

        expected_metadata_query = normalize_query("""
            CREATE TABLE IF NOT EXISTS metadata (
                id SERIAL PRIMARY KEY,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                total_records INT,
                new_records INT,
                existing_records INT
            );
        """)

        # Assert that queries were executed
        assert expected_query in executed_queries, f"Books table creation query not executed. Expected: {expected_query}"
        assert expected_metadata_query in executed_queries, "Metadata table creation query not executed."
