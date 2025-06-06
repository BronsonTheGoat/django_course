# Generated by Django 5.1.7 on 2025-04-25 17:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_application', '0008_book_available_alter_book_cover_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='library_application.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='borrows', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['borrow_date'],
            },
        ),
    ]
