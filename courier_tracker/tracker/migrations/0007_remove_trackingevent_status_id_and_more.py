# Generated by Django 5.0.6 on 2024-06-13 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_trackingevent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trackingevent',
            name='status_id',
        ),
        migrations.AddField(
            model_name='trackingevent',
            name='status_id',
            field=models.ManyToManyField(blank=True, to='tracker.status'),
        ),
    ]
