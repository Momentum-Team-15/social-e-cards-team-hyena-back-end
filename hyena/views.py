from django.shortcuts import render
from rest_framework import permissions, generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import SocialCard
from .serializers import SocialCardSerializer, CommentsSerializer, UserSerializer, StyleSerializer

# Create your views here.

class SocialCardView(generics.ListCreateAPIView):
    queryset = SocialCard.objects.all()
    serializer_class = SocialCardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.SocialCards.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

