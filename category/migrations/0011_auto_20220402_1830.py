# Generated by Django 3.2.9 on 2022-04-02 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20220402_1830'),
        ('category', '0010_remove_category_parent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]
