# Generated by Django 3.1.2 on 2020-10-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0012_auto_20201021_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='documentation_many',
            field=models.ManyToManyField(blank=True, null=True, to='manager.DocumentationMany'),
        ),
    ]
