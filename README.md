# Django Procrastinate Example

This Django project demonstrates the integration and usage of the `procrastinate` Python distributed task library with
PostgreSQL as a lightweight alternative to Celery and Redis for handling background tasks.

## Overview

This project showcases how to implement distributed task processing in Django using Procrastinate with PostgreSQL as the
task queue backend. It provides a practical example of background task processing without the need for additional
message brokers like Redis.

## Features

- Django integration with Procrastinate
- PostgreSQL-based task queue
- Example task implementation for customer data export
- Generate Procrastinate logs to the procrastinate logger
- Built-in Django admin integration
- Test data generation utility

## Requirements

- Python 3.x
- Django
- PostgreSQL
- procrastinate
- UV (Package Manager)
- Faker (for generating test data)

## Installation

1. Clone the repository
2. Install dependencies:

```bash
uv sync
```

3. Create your PostgreSQL database
4. Configure your PostgreSQL database connection in your Django .env file
4. Run migrations:

```bash
uv run manage.py migrate
```

## Project Structure

The project includes:

- Django-specific configurations for Procrastinate
- Custom tasks implementation
- Database models for storing exported files and customer data
- Management commands for generating test data

## Usage Example

### Generating Test Data

The project includes a Django management command to generate sample customer data for testing purposes:

```bash
# Generate default number of customers (50)
uv run python manage.py generate_customers
# Generate specific number of customers
uv run python manage.py generate_customers --count 20
```

This command will create random customer records with realistic data including:

- Full names
- US cities
- US state codes
- ZIP codes

### Exporting Customer Data

The project includes a sample task for exporting customer data to CSV.

1. Start a procrastinate worker in a terminal session:

```bash
uv run manage.py procrastinate worker
```

2. In a second terminal session, run the Django development server:

```bash
uv run manage.py runserver 
```

3. To trigger a customer export, you can either:
    - Use the Django admin interface (`/admin/core/exportedfile/`)
    - Use the Django shell:

```python
from core.tasks import export_customers_to_csv

export_customers_to_csv.defer()
```

The procrastinate worker will:

1. Process the export task
2. Generate a CSV file containing all customer records
3. Save the file in the `media/exports/` directory with a timestamp (format: `customers_YYYY-MM-DD_HH_MM_SS.csv`)
4. Create an `ExportedFile` record in the database

The exported CSV files will contain the following customer information:

- ID
- Name
- City
- State
- ZIP Code

You can view or access the exported files through:

- The `media/exports/` directory in your project. The file URL pattern is:
  `/media/exports/customers_YYYY-MM-DD_HH_MM_SS.csv`
- The PostgreSQL table `core_exportedfile`

You can view the procrastinate jobs through the Django admin portal at:
`http://127.0.0.1:8000/admin/procrastinate/procrastinatejob/`

Note: Make sure your `media` directory is properly configured and accessible. The project uses Django's default file
storage system with the following settings:

```python
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## Configuration

Procrastinate is configured to work with Django's default
PostgrSQL configuration, making it easy to set up and maintain.

## Benefits of Using Procrastinate

- Lightweight solution compared to Celery
- Uses PostgreSQL as task queue (no need for Redis)
- Simple integration with Django
- Built-in support for task scheduling and management

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.