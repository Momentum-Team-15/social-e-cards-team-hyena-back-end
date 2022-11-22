from django.shortcuts import render, get_object_or_404
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination
from .models import SocialCard, CustomUser, Comments
from .serializers import SocialCardSerializer, CommentsSerializer, UserSerializer, UserCreateSerializer

# Create your views here.

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'ecard_list': reverse('ecard_list', request=request, format=format),
    })

class UserView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = CustomUser.objects.filter(name=self.request.user.name)
        return queryset

class IsUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class UserListView(APIView):
    def get(self, request):
        queryset = CustomUser.objects.all()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request, view=self)
        serializer = UserSerializer(page, many=True, context={
            'request': request
        })
        return paginator.get_paginated_response(serializer.data)

class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer = UserCreateSerializer
    lookup_field = 'username'
    def get_queryset(self):
        return CustomUser.objects.all()

class CardsForUserView(APIView):
    def get(self, request, username):
        user = get_object_or_404(CustomUser, username=username)
        queryset = user.cards.all()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request, view=self)
        serializer = SocialCardSerializer(page, many=True, context={
            'request': request
        })
        return paginator.get_paginated_response(data=serializer.data)

class CardList(generics.ListCreateAPIView):
    queryset = SocialCard.objects.all()
    serializer_class = SocialCardSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SocialCard.objects.all()
    serializer_class = SocialCardSerializer
    permission_classes = (permissions.IsAuthenticated, IsUserOrReadOnly)

    def get_queryset(self):
        return SocialCard.objects.all()

class CommentsList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
