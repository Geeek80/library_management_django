# Generated by Django 2.2.2 on 2019-07-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0022_auto_20190723_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='division',
            field=models.CharField(default='a', max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='phone_no',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='resi_address',
            field=models.CharField(default='ahmedabad', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='rollno',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='semester',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
