# Generated by Django 2.2 on 2020-02-24 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_snippet_dd'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='dd',
        ),
    ]
