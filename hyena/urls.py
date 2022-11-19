from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
  path('', views.api_root),
  path('api-auth/', include('rest_framework.urls',)),
  path('ecard/', views.CardList.as_view(), name='ecard_list'),
  path('user/', views.UserView.as_view(), name='user_view'),
]


