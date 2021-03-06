# Generated by Django 2.0.2 on 2018-04-23 08:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0004_post_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('comment_text', models.TextField(validators=[django.core.validators.MinLengthValidator(3, 'atleast 3 characters')])),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_one.Post')),
            ],
        ),
    ]
