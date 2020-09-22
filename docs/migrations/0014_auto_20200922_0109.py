# Generated by Django 3.1.1 on 2020-09-22 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0013_auto_20200922_0101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='documenttype',
            options={'verbose_name': 'Document Type'},
        ),
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='docs.documenttype'),
            preserve_default=False,
        ),
    ]