# Generated by Django 4.2.10 on 2024-02-16 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0006_alter_image_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
