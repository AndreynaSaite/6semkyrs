import pytest
import uuid

from django.urls import reverse
from hypothesis import given, strategies as st, settings, HealthCheck
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

from article.models import Article, Review

User = get_user_model()

text_st = st.text(min_size=1, max_size=200)


def create_user():
    return User.objects.create_user(
        email=f"{uuid.uuid4()}@test.com",
        password="test123S1!"
    )


@pytest.mark.django_db(transaction=True)
class TestViewsFuzz:

  
    @settings(
        max_examples=15,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    @given(
        title=text_st,
        content=text_st,
        category=text_st,
    )
    def test_article_create_fuzz(self, title, content, category):
        client = APIClient()
        user = create_user()
        client.force_authenticate(user=user)

        url = reverse("create-article")

        response = client.post(url, {
            "title": title,
            "content": content,
            "category": category,
            "keywords": "test",
        }, format="json")

        assert response.status_code in (201, 400)


    
    @settings(
        max_examples=15,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    @given(query=text_st)
    def test_article_search_fuzz(self, query):
        client = APIClient()

        url = reverse("articles-list")  # FIXED NAME

        response = client.get(url + f"?search={query}")

        assert response.status_code == 200


    
    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    @given(
        text=text_st,
        rating=st.integers(min_value=1, max_value=5),
    )
    def test_review_create_fuzz(self, text, rating):
        client = APIClient()
        user = create_user()
        client.force_authenticate(user=user)

        article = Article.objects.create(
            title="t",
            content="c",
            category="cat",
            user=user,
        )

        url = reverse("review-create")

        response = client.post(url, {
            "article": article.id,
            "text": text,
            "rating": rating,
        }, format="json")

        assert response.status_code in (201, 400)



    @settings(
        max_examples=10,
        deadline=None,
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    @given(text=text_st)
    def test_review_update_fuzz(self, text):
        client = APIClient()
        user = create_user()
        client.force_authenticate(user=user)

        article = Article.objects.create(
            title="t",
            content="c",
            category="cat",
            user=user,
        )

        review = Review.objects.create(
            article=article,
            user=user,
            text="old",
            rating=3,
        )

        url = reverse("review-update", args=[review.id])

        response = client.put(url, {
            "text": text,
            "rating": 5,
        }, format="json")

        assert response.status_code in (200, 400, 404)