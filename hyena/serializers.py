from rest_framework import serializers
from .models import CustomUser, SocialCard, Comments


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name',)

class SocialCardSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = SocialCard
        fields = ('id', 'owner', 'title','border_choices', 'border_color',
                'card_color', 'font', 'text_align', 'front_message', 'back_message')

class UserCreateSerializer(serializers.ModelSerializer):
    friends = serializers.StringRelatedField(many=True, read_only=True)
    followers = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        pass

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'user', 'comment', 'card')
