from rest_framework import serializers

from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):

    poster_name = serializers.ReadOnlyField(source= 'poster_name.username')
    poster_id = serializers.ReadOnlyField(source= 'poster_name.id')

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster_name', 'poster_id', 'created']

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']
