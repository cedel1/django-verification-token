# Generated by Django 2.0 on 2018-09-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification_token', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='verificationtoken',
            name='extra_data',
            field=models.TextField(blank=True, null=True),
        ),
    ]