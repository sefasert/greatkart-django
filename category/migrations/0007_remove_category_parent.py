# Generated by Django 4.0.2 on 2022-04-01 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_category_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent',
        ),
    ]