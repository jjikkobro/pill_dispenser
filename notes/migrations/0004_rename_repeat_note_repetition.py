# Generated by Django 4.2.13 on 2024-06-15 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_note_container'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='repeat',
            new_name='repetition',
        ),
    ]