# Generated by Django 2.2.2 on 2019-07-04 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0004_auto_20190704_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymodel',
            name='image',
            field=models.FileField(default='null', upload_to=''),
            preserve_default=False,
        ),
    ]
