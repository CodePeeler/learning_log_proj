# Generated by Django 4.2.10 on 2024-02-15 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='data_added',
            new_name='date_added',
        ),
    ]