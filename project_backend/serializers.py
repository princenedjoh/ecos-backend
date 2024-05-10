from rest_framework import serializers
from .models.users_model import Users
from .models.article_model import Article
from .models.article_category_model import Article_category
from .models.article_like_model import Article_like
from .models.comment_model import Comment
from .models.comment_like_model import Comment_like
from .models.reply_model import Reply
from .models.reply_likes_model import Reply_like
from .models.mission_model import Missions
from .models.alert_model import Alert

class Users_serializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class Article_serializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class Article_category_serializer(serializers.ModelSerializer):
    class Meta:
        model = Article_category
        fields = '__all__'

class Article_like_serializer(serializers.ModelSerializer):
    class Meta:
        model = Article_like
        fields = '__all__'

class Reply_serializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class Reply_like_serializer(serializers.ModelSerializer):
    class Meta:
        model = Reply_like
        fields = '__all__'

class Comment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class Comment_like_serializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_like
        fields = '__all__'

class Missions_serializer(serializers.ModelSerializer):
    class Meta:
        model = Missions
        fields = '__all__'

class Alert_serializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = '__all__'