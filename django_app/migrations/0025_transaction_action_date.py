# Generated by Django 2.2.2 on 2019-07-26 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0024_auto_20190726_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='action_date',
            field=models.DateTimeField(blank=True, default='2019-2-1'),
            preserve_default=False,
        ),
    ]
