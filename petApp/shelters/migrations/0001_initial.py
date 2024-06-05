# Generated by Django 5.0.6 on 2024-06-01 06:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('contact_info', models.CharField(max_length=100)),
                ('staff', models.ManyToManyField(related_name='shelters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
