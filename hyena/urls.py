from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('', views.api_root),
  path('ecard/', views.CardList.as_view(), name='ecard_list')
]


