# Generated by Django 4.0.6 on 2022-12-03 14:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lms', '0005_curator_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='curator',
            name='liked_me',
            field=models.ManyToManyField(related_name='liked_curator', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='fio',
            field=models.CharField(max_length=42),
        ),
    ]
