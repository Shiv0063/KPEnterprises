# Generated by Django 5.0.3 on 2024-07-13 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_qttmodel_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotationmodel',
            name='Other',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
