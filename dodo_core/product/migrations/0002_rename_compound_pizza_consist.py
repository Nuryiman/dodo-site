# Generated by Django 5.1.3 on 2024-11-15 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='compound',
            new_name='consist',
        ),
    ]