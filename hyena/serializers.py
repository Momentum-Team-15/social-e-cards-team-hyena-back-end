from rest_framework import serializers
from .models import CustomUser, SocialCard, Style, Comments

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name',)

class SocialCardCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SocialCard
        fields = ('title', 'outer_message', 'inner_message', 'style')

class SocialCardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SocialCard
        fields = ('pk', 'owner', 'title', 'outer_message', 'inner_message', 'style', 'comments')

class StyleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Style
        fields = ('pk', 'card_color', 'border', 'border_color', 'font', 'font_color', 'text_align')
        
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('user', 'text', 'card')
