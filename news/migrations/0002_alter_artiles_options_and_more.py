# Generated by Django 4.1 on 2022-08-23 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artiles',
            options={'verbose_name': 'New', 'verbose_name_plural': 'News'},
        ),
        migrations.RenameField(
            model_name='artiles',
            old_name='full_tetx',
            new_name='full_text',
        ),
    ]
