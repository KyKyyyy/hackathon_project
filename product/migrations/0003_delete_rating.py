# Generated by Django 3.2.14 on 2022-07-28 00:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20220727_2047'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]