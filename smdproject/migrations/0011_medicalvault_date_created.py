# Generated by Django 3.2.9 on 2021-12-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smdproject', '0010_auto_20211208_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalvault',
            name='date_created',
            field=models.DateField(default='2021-08-12'),
            preserve_default=False,
        ),
    ]