# Generated by Django 2.2.2 on 2019-07-04 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_auto_20190703_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mymodel',
            options={'ordering': ['ename']},
        ),
    ]
