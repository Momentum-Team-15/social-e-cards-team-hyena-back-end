from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    # name = models.CharField(max_length=50, null=True, blank=True)
    favorites = models.ManyToManyField(
        'SocialCard', related_name='favorite_ecards', blank=True)

    avatar = models.ImageField(
        upload_to="user_avatars", blank=True, null=True)

    def __str__(self):
        return f'{self.username}'


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
    card_color = models.TextField(max_length=200, null=True)
    font = models.CharField(
        max_length=12)
    text_align = models.CharField(
        max_length=50)
    border_color = models.CharField(
        max_length=8)
    border_choices = models.CharField(
        max_length=12)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, db_index=True)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='SocialCard')

    def __str__(self):
        return f'{self.title}'


class Comments(models.Model):
    card = models.ForeignKey(
        SocialCard, on_delete=models.CASCADE, related_name='SocialCard')
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='CustomUser')
    comment = models.TextField(max_length=120)

    def __str__(self):
        return f'{self.comment}'


class Follower(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="LoggedInUser")
    being_followed = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="OtherUser")
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    created = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'being_followed'], name='unique_followers')
        ]
        ordering = ["-created"]

    # def save(self, *args, **kwargs):
    #     if self.user.is_follow.id != self.being_followed.pk:
    #         return super().save(*args, **kwargs)
    #     else:
    #         return

    def __str__(self):
        return f'{self.user} is now following {self.being_followed}'
