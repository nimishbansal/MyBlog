# Generated by Django 2.0.2 on 2018-04-25 18:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_auto_20180425_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(related_name='followd_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
