# Generated by Django 4.1.3 on 2022-11-14 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nem13', '0004_alter_accumulationmeterdata_file_path_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accumulationmeterdata',
            name='file_path',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='b2bdetails',
            name='file_path',
            field=models.CharField(max_length=240),
        ),
        migrations.AlterField(
            model_name='end',
            name='file_path',
            field=models.CharField(max_length=240),
        ),
        migrations.AddIndex(
            model_name='accumulationmeterdata',
            index=models.Index(fields=['file_path', 'nmi'], name='nem13_accum_file_pa_dc30b6_idx'),
        ),
    ]
