# Generated by Django 4.1.3 on 2022-11-14 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nem13', '0003_alter_accumulationmeterdata_previous_reason_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accumulationmeterdata',
            name='file_path',
            field=models.FilePathField(path='static'),
        ),
        migrations.AlterField(
            model_name='end',
            name='file_path',
            field=models.FilePathField(path='static'),
        ),
    ]
