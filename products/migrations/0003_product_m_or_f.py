# Generated by Django 3.2.20 on 2023-07-31 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='m_or_f',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unisex')], max_length=254, null=True),
        ),
    ]
