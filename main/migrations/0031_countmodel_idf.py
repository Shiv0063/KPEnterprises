# Generated by Django 5.0.3 on 2024-07-25 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_icountmodel_ron_invoicemodel_cluster_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='countmodel',
            name='idf',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
