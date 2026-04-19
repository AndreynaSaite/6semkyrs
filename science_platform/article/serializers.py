from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Article, Review

User = get_user_model()


# 👤 USER (публичный)
class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'first_name',
            'last_name',
        ]


# 💬 REVIEW (read)
class ReviewSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id',
            'user',
            'text',
            'rating',
            'created_at',
        ]
        read_only_fields = ['user', 'created_at']


# 💬 REVIEW (create)
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'article',
            'text',
            'rating',
        ]


# 📄 ARTICLE (READ - list/detail)
class ArticleSerializer(serializers.ModelSerializer):
    # 🔵 structured user (best practice)
    user = UserPublicSerializer(read_only=True)

    # 🟢 flattened fields (for frontend convenience)
    author_first_name = serializers.CharField(source='user.first_name', read_only=True)
    author_last_name = serializers.CharField(source='user.last_name', read_only=True)
    author_email = serializers.CharField(source='user.email', read_only=True)

    # 💬 nested reviews
    reviews = ReviewSerializer(many=True, read_only=True)
    reviews_count = serializers.IntegerField(source='reviews.count', read_only=True)

    class Meta:
        model = Article
        fields = [
            # base
            'id',
            'title',
            'content',      # preview text
            'pdf_file',
            'category',
            'keywords',
            'created_at',
            'updated_at',

            # user (structured)
            'user',

            # user (frontend-friendly)
            'author_first_name',
            'author_last_name',
            'author_email',

            # reviews
            'reviews',
            'reviews_count',
        ]


# ✍️ ARTICLE (CREATE)
class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'pdf_file',
            'category',
            'keywords',
        ]


# ✍️ ARTICLE (UPDATE)
class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'pdf_file',
            'category',
            'keywords',
        ]