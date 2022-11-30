from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_root),
    path('ecard/all/', views.CardList.as_view(), name='all-ecards'),
    path('ecard/mine/', views.CardList.as_view(), name='my-ecards'),
    path('ecard/<int:pk>/', views.CardDetail.as_view(), name='ecard_detail'),
    path('comments/', views.CommentsList.as_view(), name='comments-list'),
    path('comments/<int:pk>/', views.CommentsDetail.as_view(),
         name='comments-detail'),
    path('ecard/', views.CardDetail.as_view(), name='ecard'),
    path('users/', views.UserView.as_view(), name='user_profile'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('users/search/', views.UserSearchList.as_view(), name='search_user'),
    path('auth/users/me/avatar/', views.AvatarView.as_view(), name='user_avatar'),
    path('follower/', views.FollowerDetail.as_view(), name='follower'),
    path('follower/<int:pk>', views.FollowerEdit.as_view(), name='follower_detail'),
]
