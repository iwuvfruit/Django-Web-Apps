# Generated by Django 2.2.3 on 2019-08-02 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20190802_2138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='note_image',
            new_name='pdf',
        ),
    ]