# Generated by Django 5.0.3 on 2024-07-14 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_quotationmodel_quotationno'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrymodel',
            name='Cluster_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]