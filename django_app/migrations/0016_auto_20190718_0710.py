# Generated by Django 2.2.2 on 2019-07-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0015_auto_20190717_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='grade_history_image',
            field=models.FileField(default='null', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='last_sem_fee_image',
            field=models.FileField(default='null', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='passbook_image',
            field=models.FileField(default='null', upload_to='images/'),
            preserve_default=False,
        ),
    ]
