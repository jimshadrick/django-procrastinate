import csv
import logging
from io import StringIO  # uses an in-memory file-like object instead of a file on disk

from django.core.files.base import ContentFile  # accepts raw content instead of an actual file
from django.utils.timezone import now
from procrastinate.contrib.django import app

from core.models import Customer, ExportedFile

logger = logging.getLogger('procrastinate')


@app.task
def export_customers_to_csv():
    """
    Procrastinate task that exports all customer data to a CSV file.
    
    This asynchronous task:
    1. Retrieves all customer records from the database
    2. Creates a CSV file in memory with customer details (ID, name, location info)
    3. Generates a unique filename using current timestamp
    4. Saves the export file using the ExportedFile model
    
    The CSV includes the following columns:
    - id: Customer's unique identifier
    - name: Customer's full name
    - city: Customer's city
    - state: Customer's state
    - zipcode: Customer's ZIP code
    
    The exported file will be saved with format: customers_YYYY-MM-DD_HH_MM_SS.csv
    
    Returns:
        None. The exported file is saved to the database and filesystem via
        the ExportedFile model.
    """
    # Fetch all customers from the database
    customers = Customer.objects.all()

    # Create an in-memory buffer for CSV writing
    output = StringIO()
    writer = csv.writer(output)

    # Write header row and customer data to the CSV
    writer.writerow(['id', 'name', 'city', 'state', 'zipcode'])
    for customer in customers:
        writer.writerow([
            customer.id,
            customer.name,
            customer.city,
            customer.state,
            customer.zipcode
        ])

    # Generate unique filename with timestamp
    filename = f"customers_{now().strftime('%Y-%m-%d_%H_%M_%S')}.csv"

    # Create and save the exported file record
    export = ExportedFile()
    export.file.save(filename, ContentFile(output.getvalue()))
    export.save()
