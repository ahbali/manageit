# Generated by Django 3.1.2 on 2020-10-22 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0018_auto_20201022_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='entite_responsable',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Responsible entity'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='environment',
            field=models.CharField(blank=True, choices=[('PROD', 'Production'), ('PRE', 'Pre-production'), ('DEV', 'Development')], max_length=4, null=True, verbose_name='Environment'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_type',
            field=models.CharField(blank=True, choices=[('SRV', 'Server'), ('RTR', 'Router'), ('SW', 'Switch'), ('FWL', 'Firewall'), ('APL', 'Appliance'), ('OTHER', 'Other')], max_length=5, null=True, verbose_name='Equipment type'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='operating_system',
            field=models.CharField(blank=True, choices=[('WIN', 'Windows'), ('LINUX', 'Linux'), ('BSD', 'BSD'), ('IOS', 'CISCO IOS'), ('OTHER', 'Other')], max_length=5, null=True, verbose_name='Operating system'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='referent_technique',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.person', verbose_name='Technical Mentor'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='role',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Role'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='support',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.supportcontract', verbose_name='Support'),
        ),
        migrations.AlterField(
            model_name='equipmentdocumentation',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='Documentation/equipment', verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='equipmentdocumentation',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.equipment', verbose_name='Equipment'),
        ),
        migrations.AlterField(
            model_name='person',
            name='direction',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Direction'),
        ),
        migrations.AlterField(
            model_name='person',
            name='division',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Division'),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='person',
            name='poste_occupe',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Position'),
        ),
        migrations.AlterField(
            model_name='person',
            name='service',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Service'),
        ),
        migrations.AlterField(
            model_name='software',
            name='database_sever',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.software', verbose_name='Database server'),
        ),
        migrations.AlterField(
            model_name='software',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='software',
            name='environment',
            field=models.CharField(blank=True, choices=[('PROD', 'Production'), ('PRE', 'Pre-production'), ('DEV', 'Development')], max_length=4, null=True, verbose_name='Environment'),
        ),
        migrations.AlterField(
            model_name='software',
            name='equipment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.equipment', verbose_name='Equipment'),
        ),
        migrations.AlterField(
            model_name='software',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='software',
            name='referent_technique',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='manager.person', verbose_name='Technical Mentor'),
        ),
        migrations.AlterField(
            model_name='softwaredocumentation',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='Documentation/software', verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='softwaredocumentation',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.software', verbose_name='Software'),
        ),
        migrations.AlterField(
            model_name='sslcert',
            name='expiration_date',
            field=models.DateField(blank=True, null=True, verbose_name='Expiration date'),
        ),
        migrations.AlterField(
            model_name='sslcert',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='supportcontract',
            name='contract_date',
            field=models.DateField(blank=True, null=True, verbose_name='Contract date'),
        ),
        migrations.AlterField(
            model_name='supportcontract',
            name='expiration_date',
            field=models.DateField(blank=True, null=True, verbose_name='Expiration date'),
        ),
        migrations.AlterField(
            model_name='supportcontract',
            name='support_provider',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Support provider'),
        ),
    ]
