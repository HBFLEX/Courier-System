# Generated by Django 5.0.6 on 2024-06-11 20:36

import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_id', models.UUIDField(default=uuid.uuid4)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=15)),
                ('length', models.DecimalField(decimal_places=2, max_digits=15)),
                ('width', models.DecimalField(decimal_places=2, max_digits=15)),
                ('height', models.DecimalField(decimal_places=2, max_digits=15)),
                ('recepient_name', models.CharField(max_length=100)),
                ('sender_address', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sender_name', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Package',
                'verbose_name_plural': 'Packages',
                'ordering': ['-created_at', '-updated_at'],
            },
        ),
    ]
