# Generated by Django 2.0.3 on 2018-04-13 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0015_remove_conversationmessage_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversationmessage',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]