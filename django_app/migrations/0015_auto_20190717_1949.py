# Generated by Django 2.2.2 on 2019-07-17 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0014_librarian'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='fee_receipt_image',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]
