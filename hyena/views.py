from django.shortcuts import render
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from .models import SocialCard, CustomUser
from .serializers import SocialCardSerializer, CommentsSerializer, UserSerializer, StyleSerializer

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

class CardList(generics.ListCreateAPIView):
    queryset = SocialCard.objects.all()
    serializer_class = SocialCardSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

