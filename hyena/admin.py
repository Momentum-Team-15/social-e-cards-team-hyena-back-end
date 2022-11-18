from django.contrib import admin
from django.contrib.admin import site
from .models import CustomUser, SocialCard, Style, Comments
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(SocialCard)
admin.site.register(Style)
admin.site.register(Comments)
