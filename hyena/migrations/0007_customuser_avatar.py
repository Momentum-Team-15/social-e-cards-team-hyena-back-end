# Generated by Django 4.1.3 on 2022-11-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyena', '0006_alter_socialcard_border_choices_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='user_avatars'),
        ),
    ]
