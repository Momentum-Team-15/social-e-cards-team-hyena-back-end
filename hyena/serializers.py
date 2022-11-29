from rest_framework import serializers
from .models import CustomUser, SocialCard, Comments, Follower


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
        )


def get_following(self, obj):
    return FollowingSerializer(obj.following.all(), many=True).data


def get_followers(self, obj):
    return FollowersSerializer(obj.followers.all(), many=True).data


class SocialCardSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="username", read_only=True)

    class Meta:
        model = SocialCard
        fields = ('id', 'owner', 'title', 'border_choices', 'border_color',
                  'card_color', 'font', 'text_align', 'front_message', 'back_message', 'created_date')


class UserCreateSerializer(serializers.ModelSerializer):
    friends = serializers.StringRelatedField(many=True, read_only=True)
    followers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        pass


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('user', 'comment', 'card')


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('user', 'being_followed', 'created')


# class FollowersSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Follower
#         fields = ('user', 'created')
