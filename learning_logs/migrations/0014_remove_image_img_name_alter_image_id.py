# Generated by Django 4.2.10 on 2024-02-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0013_alter_image_img_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='img_name',
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]