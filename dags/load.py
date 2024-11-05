from sqlalchemy import create_engine
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def load_books_data(transformed_data):
    engine = create_engine('postgresql+psycopg2://airflow:airflow@postgres-books-db:5432/books_db')
    # Adjust for MySQL if needed
    try:
        with engine.connect() as connection:
            for book in transformed_data:
                title = book['title'].replace("'", "''")
                author = book['author'].replace("'", "''")
                published_date = book['published_date']
                isbn = book['isbn']

                # Safely construct the query and handle NULLs appropriately
                query = f"""
                INSERT INTO books (title, author, published_date, isbn)
                VALUES (
                    '{title}',
                    '{author}',
                    {published_date if published_date else 'NULL'},
                    '{isbn if isbn else ''}'
                )
                ON CONFLICT (isbn) DO NOTHING;
                """
                logging.info(f"Executing query: {query}")
                connection.execute(query)

        logging.info("Data loaded successfully.")
    except Exception as e:
        logging.error(f"An error occurred while loading data: {e}")
        raise
