# Generated by Django 5.1.3 on 2024-11-14 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
