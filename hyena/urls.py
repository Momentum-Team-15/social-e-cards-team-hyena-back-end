from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_root),
    path('ecard/all/', views.AllCardList.as_view(), name='all-ecards'),
    path('ecard/mine/', views.MyCardList.as_view(), name='my-ecards'),
    path('ecard/<int:pk>/', views.CardDetail.as_view(), name='ecard_detail'),
    path('users/', views.UserView.as_view(), name='user_profile'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('users/search/', views.UserSearchList.as_view(), name='search_user'),
    path('favorites/', views.FavoriteCreateView.as_view(), name='favorite-list'),
    path('favorites/<int:pk>/', views.FavoriteDetailView.as_view(), name='favorite-detail'),
]


