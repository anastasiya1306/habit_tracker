# Generated by Django 4.2.4 on 2023-08-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='chat_id',
            field=models.CharField(blank=True, null=True, verbose_name='chat_id TG'),
        ),
    ]
