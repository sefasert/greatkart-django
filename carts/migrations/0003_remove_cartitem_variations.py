# Generated by Django 4.0.2 on 2022-04-04 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_variations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='variations',
        ),
    ]
