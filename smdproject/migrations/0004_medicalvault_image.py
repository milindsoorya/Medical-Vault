# Generated by Django 3.2.9 on 2021-12-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smdproject', '0003_auto_20211207_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicalvault',
            name='image',
            field=models.ImageField(default='test', upload_to='images'),
            preserve_default=False,
        ),
    ]
