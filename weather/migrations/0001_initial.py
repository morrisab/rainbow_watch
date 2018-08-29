# Generated by Django 2.1 on 2018-08-29 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.IntegerField()),
                ('lat', models.DecimalField(decimal_places=5, max_digits=8, null=True)),
                ('lon', models.DecimalField(decimal_places=5, max_digits=8, null=True)),
            ],
        ),
    ]
