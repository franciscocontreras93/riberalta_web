# Generated by Django 3.2 on 2023-01-02 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crmcompany',
            name='industry_type',
            field=models.CharField(choices=[('', 'Select industry type'), ('Computer Industry', 'Computer Industry'), ('Chemical Industries', 'Chemical Industries'), ('Health Services', 'Health Services'), ('Telecommunications Services', 'Telecommunications Services'), ('Textiles: Clothing, Footwear', 'Textiles: Clothing, Footwear')], max_length=50),
        ),
    ]
