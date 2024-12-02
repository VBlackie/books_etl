import logging
import re


def validate_transformed_data(transformed_data):
    valid_books = []
    for book in transformed_data:
        # Check for missing critical fields
        if not book['title'] or not book['author']:
            logging.warning(f"Missing critical fields in book: {book}")
            continue

        # Handle published_date: Allow only valid years between 1500 and 2024
        try:
            # Extract year from published_date if it contains a full date (e.g., "2022-06-15")
            if isinstance(book['published_date'], str):
                match = re.match(r'^(\d{4})', book['published_date'])
                if match:
                    published_year = int(match.group(1))  # Extract the year
                else:
                    raise ValueError(f"Invalid date format: {book['published_date']}")
            else:
                published_year = int(book['published_date'])  # Convert to int directly if it's a year

            if published_year > 2024 or published_year < 1500:
                logging.warning(f"Unrealistic published_date for book: {book}")
                continue
        except (ValueError, TypeError):
            logging.warning(f"Invalid published_date format for book: {book}")
            continue

        # Check ISBN format
        if not isinstance(book['isbn'], (str, type(None))):
            logging.warning(f"Invalid ISBN format for book: {book}")
            continue

        valid_books.append(book)

    logging.info(f"Validated and kept {len(valid_books)} books out of {len(transformed_data)}.")
    return valid_books


def transform_books_data(raw_data):
    transformed_data = []
    unique_books = set()

    logging.info("Starting transformation of raw book data.")

    try:
        for book in raw_data:
            if not book['title'] or not book['author']:
                logging.warning(f"Skipping book with missing title or author: {book}")
                continue

            unique_id = book['isbn'] if book['isbn'] else (book['title'], book['author'])
            if unique_id in unique_books:
                logging.debug(f"Duplicate book found and skipped: {book['title']} by {book['author']}")
                continue

            unique_books.add(unique_id)

            transformed_data.append({
                'title': book['title'],
                'author': book['author'],
                'published_date': book['published_date'],
                'isbn': book['isbn'],
                'source': book['source']
            })

        # Validate the transformed data
        validated_data = validate_transformed_data(transformed_data)

        logging.info(f"Successfully transformed {len(validated_data)} unique books out of {len(raw_data)} raw entries.")

    except Exception as e:
        logging.critical(f"An error occurred during transformation: {e}")
        raise

    return validated_data

