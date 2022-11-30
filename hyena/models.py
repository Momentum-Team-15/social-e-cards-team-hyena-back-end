from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    def __str__(self):
        return f'{self.username}'


class SocialCard(models.Model):
    title = models.TextField(max_length=50)
    front_message = models.TextField(max_length=250)
    back_message = models.TextField(max_length=250)
    card_color = models.TextField(max_length=200, null=True)
    font = models.TextField(
        max_length=200, null=True, blank=True)
    text_align = models.TextField(
        max_length=200, null=True, blank=True)
    border_color = models.TextField(
        max_length=200, null=True, blank=True)
    border_choices = models.TextField(
        max_length=200, null=True, blank=True)
    created_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, db_index=True),
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
