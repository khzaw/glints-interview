from django.core.management.base import BaseCommand, CommandError
from book.tasks import scrape


class Command(BaseCommand):
    help = 'Scrape amazon search pages'

    def handle(self, *args, **kwargs):
        scrape()