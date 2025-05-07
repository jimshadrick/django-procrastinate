from django.db import models


class ExportedFile(models.Model):
    """
    Model to track files that are exported from the system.
    
    This model stores CSV exports of customer data, with each file being
    automatically stored in the 'exports/' directory. Each export is timestamped
    with its creation date.

    Fields:
        file (FileField): The exported file, stored in 'exports/' directory
        created_at (DateTimeField): Timestamp when the export was created
    """
    file = models.FileField(upload_to='exports/')
    created_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    """
    Model representing customer information in the system.
    
    Stores basic customer details including their name and location information.
    This data can be exported to CSV format using the associated export task.

    Fields:
        name (CharField): Customer's full name
        city (CharField): City where the customer is located
        state (CharField): State or province of the customer
        zipcode (CharField): Postal/ZIP code of the customer's location
    """
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
