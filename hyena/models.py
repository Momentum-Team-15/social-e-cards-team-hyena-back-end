from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class SocialCard(models.Model):
    image = models.ImageField(
        blank=True)
    front_message = models.TextField(250)
    back_message = models.TextField(250)
    made_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(AbstractUser)
    style = models.ForeignKey


def get_image(self):
    return self.image


def __str__(self):
    return self.front_message


class Style(models.Model):

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
        ("Bickley", "BIRCKLEY"),
        ("Brush", "BRUSH"),
        ("Comic Sans", "COMIC SANS"),
        ("Optima", "OPTIMA"),
        ("Spring", "SPRING"),
        ("Utopia", "UTOPIA"),
    )

    card_color = models.CharField(max_length=12, choices=CARD_COLOR_CHOICES)
