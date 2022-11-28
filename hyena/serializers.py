from rest_framework import serializers
from .models import CustomUser, SocialCard, Favorite


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name',)

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
        fields = ('__all__',)

class SocialCardListSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)
    owner_pk = serializers.SerializerMethodField()

    class Meta:
        model = SocialCard
        fields = ('id', 'owner', 'owner_pk', 'title', 'border_choices', 'border_color',
                'card_color', 'font', 'text_align', 'front_message', 'back_message', 'created_date')
    
    def get_owner_pk(self, obj):
        return obj.owner.id

class ModSocialCardSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    
    class Meta:
        model = SocialCard
        fields = ('id', 'owner')


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('id', 'card','user','created_at')
