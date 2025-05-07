from django.db import models


class ExportedFile(models.Model):
    """
    Model to track the files that are being exported.
    """
    file = models.FileField(upload_to='exports/')
    created_at = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
