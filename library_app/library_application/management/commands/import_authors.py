import csv

from django.core.management import BaseCommand

from ...models import Author


class Command(BaseCommand):
    help = 'Import authors from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, nargs="?", help='Input csv file', default="authors.csv")

    def handle(self, *args, **options):
        print('Import authors...')
        file_path = options['csv_file']
        try:
            with open(file_path, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    print(row)
                    if row["decease_date"] == "": row['decease_date'] = None
                    if row['decease_place'] == "": row['decease_place'] = None
                    try:
                        Author.objects.create(**row)
                    except Exception as e:
                        print(self.style.ERROR(f'Error: {e}, row {row} skipped'))

                print(Author.objects.all())

        except FileNotFoundError:
            print(self.style.ERROR(f'{file_path} does not exist.'))



