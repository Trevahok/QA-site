# Generated by Django 2.0.7 on 2018-10-24 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0008_question_modified'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-created', 'modified', 'upvotes')},
        ),
    ]
