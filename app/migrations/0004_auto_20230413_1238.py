# Generated by Django 2.2 on 2023-04-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20230413_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='image',
            field=models.ImageField(blank=True, upload_to='request_images/', verbose_name='фото'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='video',
            field=models.URLField(blank=True, max_length=100, verbose_name='ссылка на видео'),
        ),
    ]