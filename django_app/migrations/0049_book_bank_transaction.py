# Generated by Django 2.2.2 on 2019-10-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0048_auto_20191007_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='book_bank_transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'book_bank_transaction',
            },
        ),
    ]
