# Generated by Django 4.0.2 on 2022-09-06 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0005_remove_answer_answer_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='question_answer_type',
            name='question_type',
            field=models.CharField(default='xyz', max_length=100),
            preserve_default=False,
        ),
    ]
