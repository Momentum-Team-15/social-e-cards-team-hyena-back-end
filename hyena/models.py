from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to="user_avatars", blank=True, null=True)
    
    def __str__(self):
        return f'{self.username}'
        

class SocialCard(models.Model):
    title = models.TextField(max_length=50)
    front_message = models.TextField(max_length=250)
    back_message = models.TextField(max_length=250)
    card_color = models.CharField(max_length=50, null=True)
    font = models.CharField(max_length=50,  null=True, blank=True)
    text_align = models.CharField(max_length=50,null=True, blank=True)
    border_color = models.CharField(max_length=50, default='ORANGE')
    border_choices = models.CharField(max_length=50, null =True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, db_index=True),
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='SocialCard')

    def __str__(self):
        return f'{self.title}'

class Comments(models.Model):
    card = models.ForeignKey(SocialCard, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.comment
