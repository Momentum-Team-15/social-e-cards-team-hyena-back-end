from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAuthenticatedOrReadOnly, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, UpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.reverse import reverse
from rest_framework import parsers
from rest_framework.pagination import PageNumberPagination
from .models import SocialCard, CustomUser, Comments, Follower
from .serializers import SocialCardSerializer, SocialCardListSerializer, UserSerializer, ModSocialCardSerializer, CommentsSerializer, FollowingSerializer
from permissions import IsOwnerOrReadOnly
from rest_framework import filters

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'ecard_list': reverse('ecard_list', request=request, format=format),
    })


class UserView(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = CustomUser.objects.filter(username=self.request.user)
        return queryset


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer = UserSerializer


class UserSearchList(ListAPIView):
    model = CustomUser
    object_name = "quotes"
    serializer_class = UserSerializer

    def get_queryset(self):
        query = self.request.GET.get("q")
        return CustomUser.objects.annotate(search=SearchVector("username")).filter(search=query)


class IsUserOrReadOnly(BasePermission):
    def has_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user


class CardList(ListCreateAPIView):
    queryset = SocialCard.objects.all()
    serializer_class = SocialCardSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CardDetail(RetrieveUpdateDestroyAPIView):
    queryset = SocialCard.objects.all()
    serializer_class = SocialCardListSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentsList(ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class AvatarView(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    parser_classes = [parsers.FileUploadParser]

    def get_object(self):
        return self.request.user


class FollowerDetail(ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowingSerializer

    def get_queryset(self):
        queryset = Follower.objects.filter(user=self.request.user)
        return queryset
    serializer_class = FollowingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        queryset = Follower.objects.filter(user=self.request.user.id)
        return queryset


class FollowerEdit(RetrieveUpdateDestroyAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowingSerializer
