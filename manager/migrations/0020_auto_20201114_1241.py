# Generated by Django 3.1.3 on 2020-11-14 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0019_auto_20201022_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipmentdocumentation',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='softwaredocumentation',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Document'),
        ),
    ]
