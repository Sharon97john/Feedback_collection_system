# Generated by Django 4.0.2 on 2022-08-19 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0004_custom_feedback_is_published_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_type',
        ),
    ]
