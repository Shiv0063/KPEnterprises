# Generated by Django 5.0.3 on 2024-07-25 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_profilemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='icountmodel',
            name='Ron',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoicemodel',
            name='Cluster',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='invoicemodel',
            name='Cluster_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
