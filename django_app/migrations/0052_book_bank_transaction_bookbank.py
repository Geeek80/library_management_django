# Generated by Django 2.2.2 on 2019-10-08 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0051_book_bank_books_prices'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_bank_transaction',
            name='bookbank',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='django_app.book_bank'),
            preserve_default=False,
        ),
    ]
