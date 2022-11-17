from django.contrib import admin
from .models import CustomUser, SocialCard, Style, Comments

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(SocialCard)
admin.site.register(Style)
admin.site.register(Comments)