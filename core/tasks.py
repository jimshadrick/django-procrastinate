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
    customers = Customer.objects.all()
    output = StringIO()
    writer = csv.writer(output)

    # Write out the details of the customers to the in-memory buffer
    writer.writerow(['id', 'name', 'city', 'state', 'zipcode'])
    for customer in customers:
        writer.writerow([customer.id, customer.name, customer.city, customer.state,
                         customer.zipcode])

    filename = f"customers_{now().strftime('%Y-%m-%d_%H_%M_%S')}.csv"

    # Instantiate the exported file model
    export = ExportedFile()

    # Retrieve the content of the entire StringIO object and pass the content of it
    # into the ContentFile
    export.file.save(filename, ContentFile(output.getvalue()))

    export.save()
