# Generated by Django 2.1 on 2018-09-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='zip',
            field=models.CharField(max_length=5),
        ),
    ]
