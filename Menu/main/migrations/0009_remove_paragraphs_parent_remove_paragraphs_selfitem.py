# Generated by Django 4.2 on 2023-04-07 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_paragraphs_parent_alter_paragraphs_selfitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paragraphs',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='paragraphs',
            name='selfitem',
        ),
    ]
