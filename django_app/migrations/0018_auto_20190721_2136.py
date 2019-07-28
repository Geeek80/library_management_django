# Generated by Django 2.2.2 on 2019-07-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0017_auto_20190718_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=21, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='fee_receipt_image',
            field=models.FileField(blank=True, default='', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='last_sem_fee_image',
            field=models.FileField(blank=True, default='', upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='receipt_no',
            field=models.IntegerField(null=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.CharField(blank=True, default='', max_length=15),
            preserve_default=False,
        ),
    ]
