
from rest_framework import serializers
from .models import Comment
from django.contrib.auth.models import User

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='comment-highlight', format='html')

    class Meta:
        model = Comment
        fields = ('url', 'id', 'highlight', 'owner', 'content')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'comments')


    def create(self, validated_data):
        """
        Create and return a new `comment` instance, given the validated data.
        """
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `comment` instance, given the validated data.
        """
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
