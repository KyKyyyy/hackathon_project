# Generated by Django 4.0.6 on 2022-07-28 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_comment_rename_author_like_user_remove_like_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='seller',
            new_name='owner',
        ),
    ]
