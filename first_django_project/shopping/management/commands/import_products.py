import csv

from django.core.management import BaseCommand

from ...models import Product


class Command(BaseCommand):
    help = 'Import products from csv file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, nargs="?", help='Input csv file', default="products.csv")

    def handle(self, *args, **options):
#         print(args)
#         print(options)
#         print(options['csv_file'])
        print('Import products...')
        # file_path = 'products.csv'
        file_path = options['csv_file']
        try:
            with open(file_path, encoding='utf-8') as f:
                # print(f.read())
                reader = csv.DictReader(f)
                # reader = csv.reader(f, delimiter=',')
                for row in reader:
                    print(row)
                    try:
                        Product.objects.create(**row
                            # product_name=row['product_name'],
                            # price=row['price']
                        )
                    except Exception as e:
                        # print(e)
                        print(self.style.ERROR(f'Error: {e}, row {row} skipped'))

                print(Product.objects.all())

#                 print(self.style.SUCCESS(f'Products from {file_path} successfully imported.'))
#                 print(self.style.WARNING(f'Products from {file_path} successfully imported.'))
#                 print(self.style.ERROR(f'Products from {file_path} successfully imported.'))
#                 # print(self.style.__dict__)

        except FileNotFoundError:
            # print("File not found.")
            print(self.style.ERROR(f'{file_path} does not exist.'))



