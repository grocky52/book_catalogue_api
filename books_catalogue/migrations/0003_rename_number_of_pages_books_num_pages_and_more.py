# Generated by Django 4.0.6 on 2022-07-23 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_catalogue', '0002_alter_books_quantity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='number_of_pages',
            new_name='num_pages',
        ),
        migrations.RemoveField(
            model_name='books',
            name='pub_date',
        ),
    ]