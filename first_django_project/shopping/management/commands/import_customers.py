import csv

from django.core.management import BaseCommand

from ...models import Customer


class Command(BaseCommand):
    help = 'Import customers from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, nargs="?", help='Input csv file', default="customers.csv")

    def handle(self, *args, **options):
#         print(args)
#         print(options)
#         print(options['csv_file'])
        print('Import customers...')
        # file_path = 'customers.csv'
        file_path = options['csv_file']
        try:
            with open(file_path, encoding='utf-8') as f:
                # print(f.read())
                reader = csv.DictReader(f)
                # reader = csv.reader(f, delimiter=',')
                for row in reader:
                    print(row)
                    try:
                        Customer.objects.create(**row
                            # first_name=row['first_name'],
                            # last_name=row['last_name'],
                            # email=row['email'],
                            # age=row['age'],
                            # phone=row['phone'],
                        )
                    except Exception as e:
                        # print(e)
                        print(self.style.ERROR(f'Error: {e}, row {row} skipped'))

                print(Customer.objects.all())

#                 print(self.style.SUCCESS(f'Products from {file_path} successfully imported.'))
#                 print(self.style.WARNING(f'Products from {file_path} successfully imported.'))
#                 print(self.style.ERROR(f'Products from {file_path} successfully imported.'))
#                 # print(self.style.__dict__)

        except FileNotFoundError:
            # print("File not found.")
            print(self.style.ERROR(f'{file_path} does not exist.'))



