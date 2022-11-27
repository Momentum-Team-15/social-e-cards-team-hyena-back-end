from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    # name = models.CharField(max_length=50, null=True, blank=True)
    favorites = models.ManyToManyField(
        'SocialCard', related_name='favorite_ecards', blank=True)

    def __str__(self):
        return f'{self.username}'

    def __str__(self):
        return self.username


class SocialCard(models.Model):
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

    title = models.CharField(max_length=50)
    front_message = models.TextField(max_length=250)
    back_message = models.TextField(max_length=250)
    card_color = models.TextField(max_length=200)
    font = models.CharField(
        max_length=12, choices=FONT_CHOICES, null=True, blank=True)
    text_align = models.CharField(
        max_length=50, choices=TEXT_ALIGNMENT_CHOICES, null=True, blank=True)
    border_color = models.CharField(
        max_length=8, choices=BORDER_COLOR, default='ORANGE')
    border_choices = models.CharField(
        max_length=12, choices=BORDER_CHOICES, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='SocialCard')

    def __str__(self):
        return f'{self.title}'


class Comments(models.Model):
    card = models.ForeignKey(SocialCard, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField(max_length=120)

    def __str__(self):
        return f'{self.comment}'


class Follower(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="LoggedInUser")
    being_followed = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="OtherUser")

    def __str__(self):
        return f'{self.user} is now following {self.being_followed}'
