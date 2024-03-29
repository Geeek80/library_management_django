# Generated by Django 2.2.2 on 2019-08-01 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0029_auto_20190728_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.AddField(
            model_name='student',
            name='application_no',
            field=models.CharField(default='ica17_c_1', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='stream',
            field=models.CharField(default='ica', max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='reason',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
