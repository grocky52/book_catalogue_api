# Generated by Django 4.0.6 on 2022-07-23 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]