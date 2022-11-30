from rest_framework import serializers
from .models import CustomUser, SocialCard, Comments
from datetime import datetime
import json

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'avatar')

    def update(self, instance, validated_data):
        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.avatar.save(file.name, file, save=True)
            return instance
        return super().update(instance, validated_data)

class UserCreateSerializer(serializers.ModelSerializer):
    friends = serializers.StringRelatedField(many=True, read_only=True)
    followers = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        pass

class SocialCardSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    
    class Meta:
        model = SocialCard
        fields = ('id', 'owner', 'title', 'border_choices', 'border_color',
                'card_color', 'font', 'text_align', 'front_message', 'back_message', 'created_date')

class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comments
        fields = ('id', 'card','comment','user')
