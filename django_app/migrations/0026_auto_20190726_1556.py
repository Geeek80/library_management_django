# Generated by Django 2.2.2 on 2019-07-26 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0025_transaction_action_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(blank=True, max_length=21, null=True),
        ),
    ]