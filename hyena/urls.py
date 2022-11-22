from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_root),
    path('ecard/', views.CardList.as_view(), name='ecard_list'),
    path('ecard/<int:pk>/', views.CardDetail.as_view(), name='ecard_detail'),
    path('comments/', views.CommentsList.as_view(), name='comments-list'),
    path('comments/<int:pk>/', views.CommentsDetail.as_view(), name='comments-detail'),
    path('users/', views.UserView.as_view(), name='user_profile'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('users/search/', views.UserSearchList.as_view(), name='search_user'),
]


