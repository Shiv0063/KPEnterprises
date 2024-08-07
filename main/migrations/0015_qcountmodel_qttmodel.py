# Generated by Django 5.0.3 on 2024-06-15 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_invoicemodel_partyname'),
    ]

    operations = [
        migrations.CreateModel(
            name='QCountModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuotationNo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='QTTModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Counter', models.IntegerField(blank=True, default=0, null=True)),
                ('RCCode', models.CharField(blank=True, max_length=100, null=True)),
                ('RCDescription', models.TextField(blank=True, null=True)),
                ('Quantity', models.CharField(blank=True, max_length=100, null=True)),
                ('Rate', models.CharField(blank=True, default='0', max_length=100, null=True)),
                ('Labour', models.CharField(blank=True, default='0', max_length=100, null=True)),
                ('Amount', models.CharField(blank=True, default='0', max_length=100, null=True)),
            ],
        ),
    ]
