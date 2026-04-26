from rest_framework import generics, permissions, filters
from .models import Article, Review
from .serializers import ArticleSerializer, ArticleCreateSerializer, ReviewSerializer, ReviewCreateSerializer
from rest_framework.response import Response

class ArticleCreateView(generics.CreateAPIView):
    queryset = Article.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ArticleCreateSerializer
        return ArticleSerializer

    def perform_create(self, serializer):
        self.instance = serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = serializer.save(user=request.user)

        response_serializer = ArticleSerializer(article)

        return Response(response_serializer.data, status=201)
    

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'keywords', 'content']


class MyArticlesView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Article.objects.filter(user=self.request.user).order_by('-created_at')
    
class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return Review.objects.filter(article_id=article_id).order_by('-created_at')
    
class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewUpdateView(generics.UpdateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)
    
class ReviewDeleteView(generics.DestroyAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)