from django.shortcuts import render

from core.tasks import export_customers_to_csv


# Create your views here.
def index(request):
    # Launch the task
    export_customers_to_csv.defer()
    return render(request, 'index.html')
