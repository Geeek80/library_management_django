# Generated by Django 2.2.2 on 2019-09-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0044_auto_20190926_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountant',
            name='phone_no',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='accountant',
            name='resi_address',
            field=models.CharField(default='ahmedabad', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='librarian',
            name='phone_no',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='librarian',
            name='resi_address',
            field=models.CharField(default='ahmedabad', max_length=150),
            preserve_default=False,
        ),
    ]
