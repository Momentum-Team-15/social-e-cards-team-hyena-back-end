from django.shortcuts import render, get_object_or_404
from django.contrib.postgres.search import SearchVector
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.pagination import PageNumberPagination
from .models import SocialCard, CustomUser, Comments, Follower
from .serializers import SocialCardSerializer, CommentsSerializer, UserSerializer, UserCreateSerializer, FollowerSerializer

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'ecard_list': reverse('ecard_list', request=request, format=format),
    })


<< << << < HEAD


class UserView(generics.ListCreateAPIView):


== == == =
class UserView(ListCreateAPIView):


>>>>>> > main
  queryset = CustomUser.objects.all()
   serializer_class = UserSerializer

    def get_queryset(self):
        queryset = CustomUser.objects.filter(username=self.request.user)
        return queryset

<< << << < HEAD


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer = UserSerializer


class UserSearchList(generics.ListAPIView):


== == == =


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer = UserSerializer


class UserSearchList(ListAPIView):


>>>>>> > main
  model = CustomUser
   object_name = "quotes"
    serializer_class = UserSerializer

    def get_queryset(self):
        query = self.request.GET.get("q")
        return CustomUser.objects.annotate(search=SearchVector("username")).filter(search=query)

<< << << < HEAD


class IsUserOrReadOnly(permissions.BasePermission):


== == == =
class IsUserOrReadOnly(BasePermission):


>>>>>> > main
  def has_permission(self, request, view, obj):
       if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user

<< <<<< < HEAD


class CardList(generics.ListCreateAPIView):
== == ===
class CardList(ListCreateAPIView):

>>>>>> > main
  queryset = SocialCard.objects.all()
   serializer_class = SocialCardSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

<< <<<< < HEAD


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
== == ===
class CardDetail(RetrieveUpdateDestroyAPIView):

>>>>>> > main
  queryset = SocialCard.objects.all()
   serializer_class = SocialCardSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SocialCard.objects.all()


<< <<<< < HEAD
class CommentsList(generics.ListCreateAPIView):
== == ===
class CommentsList(ListCreateAPIView):

>>>>>> > main
  queryset = Comments.objects.all()
   serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

<< <<<< < HEAD


class CommentsDetail(generics.RetrieveUpdateDestroyAPIView):
== == ===
class CommentsDetail(RetrieveUpdateDestroyAPIView):

>>>>>> > main
  queryset = Comments.objects.all()
   serializer_class = CommentsSerializer


class FollowerView(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def get_queryset(self):
        queryset = Follower.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
