from rest_framework import serializers

from gpost_app.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'boast_roast',
            'up_field',
            'down_field',
            'votes',
            'post_date'
        ]