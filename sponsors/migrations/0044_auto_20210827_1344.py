# Generated by Django 2.0.13 on 2021-08-27 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0043_auto_20210827_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorship',
            name='level_name_old',
            field=models.CharField(blank=True, default='', help_text='DEPRECATED: shall be removed after manual data sanity check.', max_length=64, verbose_name='Level name'),
        ),
    ]