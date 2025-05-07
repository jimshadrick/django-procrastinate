"""
Django management command to generate random customer data.
"""
import random

from django.core.management.base import BaseCommand
from faker import Faker

from core.models import Customer


class Command(BaseCommand):
    help = 'Generate random customers for testing'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=50, help='Number of customers to create')

    def handle(self, *args, **options):
        count = options['count']
        fake = Faker()

        # List of US states for more realistic data
        states = [
            'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
            'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD',
            'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
            'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
            'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
        ]

        self.stdout.write(f"Creating {count} random customers...")

        for i in range(count):
            name = fake.name()
            city = fake.city()
            state = random.choice(states)
            zipcode = fake.zipcode()

            Customer.objects.create(
                name=name,
                city=city,
                state=state,
                zipcode=zipcode
            )

            if (i + 1) % 10 == 0:
                self.stdout.write(f"Created {i + 1} customers so far...")

        self.stdout.write(self.style.SUCCESS(f"Successfully created {count} customers!"))
