# Generated by Django 2.0.2 on 2018-04-25 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0008_auto_20180425_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('email_text', models.TextField(max_length=20000)),
                ('email_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('email_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emitter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
