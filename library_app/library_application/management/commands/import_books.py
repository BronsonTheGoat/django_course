import csv

from django.core.management import BaseCommand

from ...models import Book


class Command(BaseCommand):
    help = 'Import books from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, nargs="?", help='Input csv file', default="books.csv")

    def handle(self, *args, **options):
        print('Import books...')
        file_path = options['csv_file']
        try:
            with open(file_path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    print(row)
                    try:
                        Book.objects.create(**row)
                    except Exception as e:
                        print(self.style.ERROR(f'Error: {e}, row {row} skipped'))

                print(Book.objects.all())

        except FileNotFoundError:
            print(self.style.ERROR(f'{file_path} does not exist.'))



