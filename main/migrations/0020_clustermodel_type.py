# Generated by Django 5.0.3 on 2024-07-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_partynamemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='clustermodel',
            name='Type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
