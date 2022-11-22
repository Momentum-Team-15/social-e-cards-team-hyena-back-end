from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_root),
    path('ecard/', views.CardList.as_view(), name='ecard_list'),
    path('ecard/<int:pk>/', views.CardDetail.as_view(), name='ecard_detail'),
    path('comments/', views.CommentsList.as_view(), name='comments-list'),
    path('comments/<int:pk>/', views.CommentsDetail.as_view(), name='comments-detail'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('users/<username>/cards/', views.CardsForUserView.as_view()),
    path('user-detail/<username>', views.UserDetailView.as_view(), name='user-list'),
]


