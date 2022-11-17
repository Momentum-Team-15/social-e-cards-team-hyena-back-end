from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from hyena import views

urlpatterns = [
    path('', views.api_root),
    path('ecard/', views.CardList.as_view(), name='ecard_list'),
    ]
