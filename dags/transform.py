import logging


def validate_transformed_data(transformed_data):
    for book in transformed_data:
        if not book['title'] or not book['author']:
            logging.warning(f"Missing critical fields in book: {book}")
        if book['published_date'] and (book['published_date'] > 2024 or book['published_date'] < 1500):
            logging.warning(f"Unrealistic published_date for book: {book}")
        if not isinstance(book['isbn'], (str, type(None))):
            logging.warning(f"Invalid ISBN format for book: {book}")
    logging.info("Transformed data validated successfully.")


def transform_books_data(raw_data):
    transformed_data = []
    unique_books = set()  # Set to store unique identifiers (ISBN or title-author pairs)

    # Log the start of the transformation process
    logging.info("Starting transformation of raw book data.")

    try:
        for book in raw_data:
            # Skip entries with missing title or author and log a warning
            if not book['title'] or not book['author']:
                logging.warning(f"Skipping book with missing title or author: {book}")
                continue

            # Use ISBN if available, otherwise use a combination of title and author as the unique identifier
            unique_id = book['isbn'] if book['isbn'] else (book['title'], book['author'])

            # Check if the unique_id is already in the set
            if unique_id in unique_books:
                logging.debug(f"Duplicate book found and skipped: {book['title']} by {book['author']}")
                continue  # Skip this book as it's a duplicate

            # Add the unique_id to the set
            unique_books.add(unique_id)

            # Add the book to the transformed_data list
            transformed_data.append({
                'title': book['title'],
                'author': book['author'],
                'published_date': book['published_date'],
                'isbn': book['isbn'],
                'source': book['source']
            })
        validate_transformed_data(transformed_data)  # Add validation here

        # Log the result of the transformation
        logging.info(f"Successfully transformed {len(transformed_data)} unique books out of {len(raw_data)} raw entries.")

    except Exception as e:
        # Log any unexpected error that occurs during transformation
        logging.critical(f"An error occurred during transformation: {e}")
        raise

    return transformed_data
