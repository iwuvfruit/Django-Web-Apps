# Generated by Django 2.2.3 on 2019-08-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_delete_featured'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectIdea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='get_image_path_quotes')),
                ('person', models.CharField(max_length=128)),
                ('quote', models.TextField()),
            ],
        ),
    ]
