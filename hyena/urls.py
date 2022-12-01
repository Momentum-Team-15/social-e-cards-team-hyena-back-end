from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root),
    path('ecard/', views.CardListCreate.as_view(), name='ecard'),
    path('ecard/<int:pk>/', views.CardDetail.as_view(), name='ecard_detail'),
    path('ecard/', views.CardDetail.as_view(), name='ecard'),
    path('ecard/mine/', views.MyCards.as_view(), name='my_ecards'),
    path('users/', views.UserView.as_view(), name='user_profile'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('users/search/', views.UserSearchList.as_view(), name='search_user'),
    path('follower/', views.FollowerDetail.as_view(), name='follower'),
    path('follower/<int:pk>', views.FollowerEdit.as_view(), name='follower_detail'),
    path('comment/', views.CommentListCreate.as_view(), name='comment'),
    path('comment/<int:pk>/', views.CommentsDetail.as_view(), name='comment_detail'),
    path('auth/users/me/avatar/', views.UserAvatarView.as_view(), name="user_avatar"),
]
