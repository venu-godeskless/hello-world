# Generated by Django 2.2 on 2020-02-20 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_new', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_student',
            name='age',
            field=models.IntegerField(),
        ),
    ]
