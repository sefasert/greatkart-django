# Generated by Django 4.0.2 on 2022-04-05 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0011_auto_20220402_1830'),
        ('store', '0013_delete_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='category.category'),
        ),
    ]
