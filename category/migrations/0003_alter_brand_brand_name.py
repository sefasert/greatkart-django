# Generated by Django 4.0.2 on 2022-03-31 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_brand_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=50, null=True),
        ),
    ]
