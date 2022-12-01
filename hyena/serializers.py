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

    def update(self, instance, validated_data):
        if "file" in self.initial_data:
            file = self.initial_data.get("file")
            instance.avatar.save(file.name, file, save=True)
            return instance
        # this call to super is to make sure that update still works for other fields
        return super().update(instance, validated_data)


class UserCreateSerializer(serializers.ModelSerializer):
    friends = serializers.StringRelatedField(many=True, read_only=True)
    followers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        pass


class SocialCardSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="username", read_only=True)

    class Meta:
        model = SocialCard
        fields = ('id', 'title', 'front_message', 'back_message', 'card_color',
                  'font', 'text_align', 'border_color', 'border_choices', 'owner')


class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comments
        fields = ('id', 'card', 'comment', 'user')


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ('id', 'user', 'being_followed', 'created')
