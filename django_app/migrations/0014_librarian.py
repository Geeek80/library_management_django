# Generated by Django 2.2.2 on 2019-07-12 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0013_student_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=21)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'librarian',
            },
        ),
    ]