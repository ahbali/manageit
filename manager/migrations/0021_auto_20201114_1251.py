# Generated by Django 3.1.3 on 2020-11-14 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0020_auto_20201114_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='documentation_many',
        ),
        migrations.DeleteModel(
            name='DocumentationMany',
        ),
    ]