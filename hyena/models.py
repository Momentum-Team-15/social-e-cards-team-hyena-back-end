from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    pass


class Style(models.Model):

    TEXT_ALIGNMENT_CHOICES = (
        ('LEFT', 'LEFT'),
        ('CENTER', 'CENTER'),
        ('RIGHT', 'RIGHT')
    )

    CARD_COLOR_CHOICES = (
        ("White", "WHITE"),
        ("Red", "RED"),
        ("Blue", "BLUE"),
        ("Green", "GREEN"),
        ("Yellow", "YELLOW"),
        ("Pink", "PINK"),
    )

    FONT_CHOICES = (
        ("American", "AMERICAN"),
        ("Birckley", "BIRCKLEY"),
        ("Brush", "BRUSH"),
        ("Comic Sans", "COMIC SANS"),
        ("Optima", "OPTIMA"),
        ("Spring", "SPRING"),
        ("Utopia", "UTOPIA"),
    )

    BORDER_COLOR = (
        ("White", "WHITE"),
        ("Red", "RED"),
        ("Blue", "BLUE"),
        ("Green", "GREEN"),
        ("Yellow", "YELLOW"),
        ("Pink", "PINK"),
        ("Purple", "PURPLE"),
        ("Orange", "ORANGE"),
    )

    BORDER_CHOICES = (
        ("SOLID", "Solid"),
        ("DASHED", "Dashed"),
        ("DOTTED", "Dotted"),
        ("DOUBLE", "Double"),
        ("HAIR", "Hair"),
        ("MEDIUM", "Medium"),
        ("DASHDOT", "Dashdot"),
    )
    card_color = models.CharField(max_length=6, choices=CARD_COLOR_CHOICES)
    font = models.CharField(max_length=12, choices=FONT_CHOICES)
    border_color = models.CharField(max_length=8, choices=BORDER_COLOR)
    border_choices = models.CharField(max_length=12, choices=BORDER_CHOICES)


class SocialCard(models.Model):
    title = models.CharField(max_length=50)
    front_message = models.TextField(250)
    back_message = models.TextField(250)
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    style = models.ForeignKey(Style, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=120)
    card = models.ForeignKey(SocialCard, on_delete=models.CASCADE)
