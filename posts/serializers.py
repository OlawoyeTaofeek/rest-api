from rest_framework import serializers

from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    poster_name = serializers.ReadOnlyField(source= 'poster_name.username')
    poster_id = serializers.ReadOnlyField(source= 'poster_name.id')
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'poster_name', 'poster_id', 'created', 'votes']
    #Getting the vote
    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id']
