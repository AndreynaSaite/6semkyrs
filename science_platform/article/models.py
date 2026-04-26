from django.db import models
from django.conf import settings

class Article(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles'
    )

    title = models.CharField(max_length=255)

    content = models.TextField()

    pdf_file = models.FileField(upload_to='pdfs/')

    category = models.CharField(max_length=100)

    keywords = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    text = models.TextField()
    rating = models.IntegerField(default=5)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user.email}"