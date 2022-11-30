from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root),
    path('ecard/', views.CardListCreate.as_view(), name='ecard'),
    path('ecard/<int:pk>/', views.CardDetail.as_view(), name='ecard_detail'),
    path('comments/', views.CommentListCreateView.as_view(), name='comments_list'),
    path('comments/<int:pk>/', views.CommentsDetail.as_view(), name='comments_detail_detail'),
    path('users/', views.UserView.as_view(), name='user_profile'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('users/search/', views.UserSearchList.as_view(), name='search_user'),
    path('auth/users/me/avatar/', views.AvatarView.as_view(), name='user_avatar')
]



