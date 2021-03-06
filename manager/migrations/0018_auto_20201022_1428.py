# Generated by Django 3.1.2 on 2020-10-22 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0017_auto_20201022_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='end_of_life',
            field=models.DateField(blank=True, null=True, verbose_name='End of life'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='entite_responsable',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='environment',
            field=models.CharField(blank=True, choices=[('PROD', 'Production'), ('PRE', 'Pre-production'), ('DEV', 'Development')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_type',
            field=models.CharField(blank=True, choices=[('SRV', 'Server'), ('RTR', 'Router'), ('SW', 'Switch'), ('FWL', 'Firewall'), ('APL', 'Appliance'), ('OTHER', 'Other')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='license_end',
            field=models.DateField(blank=True, null=True, verbose_name='License end'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='operating_system',
            field=models.CharField(blank=True, choices=[('WIN', 'Windows'), ('LINUX', 'Linux'), ('BSD', 'BSD'), ('IOS', 'CISCO IOS'), ('OTHER', 'Other')], max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='ship_to_prod_date',
            field=models.DateField(blank=True, null=True, verbose_name='Production date'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='virt_phys',
            field=models.CharField(blank=True, choices=[('VIRT', 'Virtual'), ('PHYS', 'Physical')], max_length=4, null=True, verbose_name='Virtual/Physical'),
        ),
        migrations.AlterField(
            model_name='person',
            name='direction',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='division',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='poste_occupe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='service',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='software',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='software',
            name='environment',
            field=models.CharField(blank=True, choices=[('PROD', 'Production'), ('PRE', 'Pre-production'), ('DEV', 'Development')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='software',
            name='ship_to_prod_date',
            field=models.DateField(blank=True, null=True, verbose_name='Production date'),
        ),
        migrations.AlterField(
            model_name='sslcert',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sslcert',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='supportcontract',
            name='contract_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supportcontract',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='supportcontract',
            name='support_provider',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
