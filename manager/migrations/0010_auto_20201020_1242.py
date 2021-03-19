# Generated by Django 3.1.2 on 2020-10-20 11:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20201009_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentation',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('documentation', models.FileField(blank=True, null=True, upload_to='Documentation/%Y/%m/%d')),
            ],
        ),
        migrations.AddField(
            model_name='equipment',
            name='docs',
            field=models.ManyToManyField(to='manager.Documentation'),
        ),
    ]