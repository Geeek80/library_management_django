# Generated by Django 2.2.2 on 2019-08-24 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0038_transaction_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='temp',
        ),
    ]
