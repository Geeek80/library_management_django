# Generated by Django 2.2.2 on 2019-10-08 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0050_book_bank_transaction_studentt'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_bank',
            name='books_prices',
            field=models.CharField(default=100, max_length=30),
            preserve_default=False,
        ),
    ]
