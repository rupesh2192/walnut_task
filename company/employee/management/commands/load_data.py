import json
import csv
from django.core.management import BaseCommand

from employee.models import Employee
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """
    This command accepts optional argument -d or --datafile, which should be a JSOn file containing initial data.
    It imports the data from the JSON file into the database for Movie, Genre and Directors table.
    """
    help = "Load data from JSON file"

    def add_arguments(self, parser):
        parser.add_argument("-d", "--data_file", type=str, default="imdb_data.json")

    def handle(self, *args, **options):
        logger.info("Starting to load data from file: options['data_file']")

        Employee.objects.filter(is_staff=False).delete()
        data = csv.DictReader(open("us-500.csv"))
        emp_list = []
        for employee in data:
            emp_list.append(Employee(first_name=employee["first_name"],
                         last_name=employee["last_name"],
                         email=employee["email"],
                         is_staff=False,
                         username=employee["email"]
                         ))
        Employee.objects.bulk_create(emp_list)
        logger.info("Data import completed successfully")
