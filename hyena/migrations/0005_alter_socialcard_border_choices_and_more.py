# Generated by Django 4.1.3 on 2022-11-30 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyena', '0004_remove_customuser_avatar_remove_customuser_favorites_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialcard',
            name='border_choices',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='socialcard',
            name='border_color',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='socialcard',
            name='font',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='socialcard',
            name='text_align',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]