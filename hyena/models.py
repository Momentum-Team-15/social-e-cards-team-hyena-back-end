from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    about = models
    favorites = models.ManyToManyField('SocialCard', related_name='favorite_ecards', blank=True)
    def __str__(self):
        return f'{self.username}'

class SocialCard(models.Model):
    title = models.CharField(max_length=50)
    front_message = models.TextField(max_length=250)
    back_message = models.TextField(max_length=250)
    card_color = models.CharField(max_length=100, null=True, default='white')
    font = models.CharField(max_length=100, null=True, blank=True)
    text_align = models.CharField(max_length=100, null=True, blank=True)
    border_color = models.CharField(max_length=100, default='white')
    border_choices = models.CharField(max_length=100, default='solid', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title}'


class Comments(models.Model):
    card = models.ForeignKey(SocialCard, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    comment = models.TextField(max_length=120)

    def __str__(self):
        return f'{self.comment}'
    
