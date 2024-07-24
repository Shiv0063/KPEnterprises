# Generated by Django 5.0.3 on 2024-07-24 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_alter_entrymodel_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(blank=True, max_length=100, null=True)),
                ('CompanyName', models.CharField(blank=True, max_length=100, null=True)),
                ('PhoneNo', models.CharField(blank=True, max_length=100, null=True)),
                ('GSTNo', models.CharField(blank=True, max_length=100, null=True)),
                ('PanNo', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('Address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]