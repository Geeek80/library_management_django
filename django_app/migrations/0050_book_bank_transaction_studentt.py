# Generated by Django 2.2.2 on 2019-10-08 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0049_book_bank_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_bank_transaction',
            name='studentt',
            field=models.ForeignKey(default=16, on_delete=django.db.models.deletion.CASCADE, to='django_app.student'),
            preserve_default=False,
        ),
    ]