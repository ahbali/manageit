# Generated by Django 3.1.2 on 2020-10-22 08:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0014_auto_20201021_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentationsEquipment',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('document', models.FileField(blank=True, null=True, upload_to='Documentation/equipment')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentationsSoftware',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('document', models.FileField(blank=True, null=True, upload_to='Documentation/software')),
            ],
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='documentation',
        ),
        migrations.RemoveField(
            model_name='software',
            name='documentation',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='fqdn',
            field=models.CharField(blank=True, max_length=1000, null=True, validators=[django.core.validators.RegexValidator(code='invalid', message='Only alphanumeric characters, hyphens, periods, and underscores are allowed in DNS names', regex='^[0-9A-Za-z._-]+$')], verbose_name='FQDN'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='operating_system',
            field=models.CharField(choices=[('WIN', 'Windows'), ('LINUX', 'Linux'), ('BSD', 'BSD'), ('IOS', 'CISCO IOS'), ('OTHER', 'Other')], default='LINUX', max_length=5),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='ship_to_prod_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Production date'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='virt_phys',
            field=models.CharField(choices=[('VIRT', 'Virtual'), ('PHYS', 'Physical')], default='PHYS', max_length=4, verbose_name='Virtual/Physical'),
        ),
        migrations.AlterField(
            model_name='software',
            name='ship_to_prod_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Production date'),
        ),
        migrations.DeleteModel(
            name='DocumentationsForeign',
        ),
        migrations.AddField(
            model_name='documentationssoftware',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.software'),
        ),
        migrations.AddField(
            model_name='documentationsequipment',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.equipment'),
        ),
    ]
