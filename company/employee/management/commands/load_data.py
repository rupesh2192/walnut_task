import json

from django.core.management import BaseCommand

from movies.models import Movie, Genre, Director
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

        Movie.objects.all().delete()
        data = json.load(open(options["data_file"]))
        for movie in data:
            temp = Movie(popularity=movie["99popularity"],
                         imdb_score=movie["imdb_score"],
                         name=movie["name"])
            temp.director = Director.objects.get_or_create(name=movie["director"].strip())[0]
            temp.save()
            genre_list = list()
            for genre in movie["genre"]:
                obj, created = Genre.objects.get_or_create(name=genre.strip())
                genre_list.append(obj)
            temp.genre.set(genre_list)

        logger.info("Data import completed successfully")
