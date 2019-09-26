# Generated by Django 2.2.2 on 2019-09-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0043_auto_20190920_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='accountant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('password', models.CharField(max_length=21)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'accountant',
            },
        ),
        migrations.AlterField(
            model_name='librarian',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]