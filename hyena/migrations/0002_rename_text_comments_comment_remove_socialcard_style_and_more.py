# Generated by Django 4.1.3 on 2022-11-21 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyena', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='text',
            new_name='comment',
        ),
        migrations.RemoveField(
            model_name='socialcard',
            name='style',
        ),
        migrations.AddField(
            model_name='socialcard',
            name='border_choices',
            field=models.CharField(blank=True, choices=[('SOLID', 'Solid'), ('DASHED', 'Dashed'), ('DOTTED', 'Dotted'), ('DOUBLE', 'Double'), ('HAIR', 'Hair'), ('MEDIUM', 'Medium'), ('DASHDOT', 'Dashdot')], max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='socialcard',
            name='border_color',
            field=models.CharField(choices=[('White', 'WHITE'), ('Red', 'RED'), ('Blue', 'BLUE'), ('Green', 'GREEN'), ('Yellow', 'YELLOW'), ('Pink', 'PINK'), ('Purple', 'PURPLE'), ('Orange', 'ORANGE')], default='ORANGE', max_length=8),
        ),
        migrations.AddField(
            model_name='socialcard',
            name='card_color',
            field=models.CharField(choices=[('White', 'WHITE'), ('Red', 'RED'), ('Blue', 'BLUE'), ('Green', 'GREEN'), ('Yellow', 'YELLOW'), ('Pink', 'PINK')], default='YELLOW', max_length=6),
        ),
        migrations.AddField(
            model_name='socialcard',
            name='font',
            field=models.CharField(blank=True, choices=[('American', 'AMERICAN'), ('Birckley', 'BIRCKLEY'), ('Brush', 'BRUSH'), ('Comic Sans', 'COMIC SANS'), ('Optima', 'OPTIMA'), ('Spring', 'SPRING'), ('Utopia', 'UTOPIA')], max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='socialcard',
            name='back_message',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='socialcard',
            name='front_message',
            field=models.TextField(max_length=250),
        ),
        migrations.DeleteModel(
            name='Style',
        ),
    ]
