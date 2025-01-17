# Generated by Django 5.1.3 on 2024-11-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customerprofile',
            options={'verbose_name': 'Customer Profile', 'verbose_name_plural': 'Customer Profiles'},
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
