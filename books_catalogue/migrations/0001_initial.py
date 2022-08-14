# Generated by Django 4.0.6 on 2022-07-22 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('number_of_pages', models.IntegerField()),
                ('quantity', models.BigIntegerField()),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
