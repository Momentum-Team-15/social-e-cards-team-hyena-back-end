from django.urls import path, include
from . import views

path('', views.api_root),
path('ecard/', views.CardList.as_view(), name='ecard_list'),
path('cards/',views.CardView.as_view(), name='card-list'),
path('cards/me/', include('rest_framework.urls')),
path('cards/all/', views.BookView.as_view(), name='book-list'),
path('cards/:id', views.BookViewSet.as_view({'get': 'list'}), name='book-list'),
path('friends/', views.NoteView.as_view(), name='note-list'),
path('friends/:user_id/', views.NoteView.as_view(), name='note-add'),

