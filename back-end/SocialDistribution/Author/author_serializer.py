from rest_framework import serializers
from . import models 


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ["id", "displayName", "host", "url", "type", "github"]
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ["type","post_id","title", "description",
                  "source", "origin", "contentType", "content", "categories",
                  "commentLink", "commentCount", "pageSize", "published",
                  "visibility", "unlisted"]

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FriendShip
        fields = ["FriendshipId", "author_primary", "author_friend", "accepted"]

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = ["like_id", "author_id", "object_id", "liker_id"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ["comment_id", "post_id", "contentType", "published",
                  "comment", "type"]

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Notification
        fields = ["notification_id", "author_id", "request_id", "like_id", 
                  "comment_id", "post_id"]
