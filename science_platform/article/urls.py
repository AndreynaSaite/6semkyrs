from django.urls import path
from .views import ArticleCreateView, ArticleListView, MyArticlesView, ReviewDeleteView, ReviewCreateView, ReviewListView, ReviewUpdateView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('create/', ArticleCreateView.as_view(), name='create-article'),
    path('articles/', ArticleListView.as_view(), name='articles-list'),
    path('my-articles/', MyArticlesView.as_view(), name='my-articles'),
    path('review-create/', ReviewCreateView.as_view(), name='review-create'),
    path('review-list/<int:article_id>/', ReviewListView.as_view(), name='review-list'),
    path('review-update/<int:pk>/', ReviewUpdateView.as_view(), name='review-update'),
    path('review-delete/<int:pk>/', ReviewDeleteView.as_view(), name='review-delete'),
]
