# Generated by Django 4.0.4 on 2022-05-03 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appBlog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='edad',
            new_name='codigo',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='correo',
        ),
    ]
