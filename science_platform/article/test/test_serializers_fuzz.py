import pytest
from hypothesis import given, settings, strategies as st, HealthCheck
from django.contrib.auth import get_user_model

from accounts.serializers import RegisterSerializer
from article.serializers import (
    ArticleCreateSerializer,
    ReviewCreateSerializer,
)

User = get_user_model()


emails = st.emails().map(lambda e: f"u_{e}")

text = st.text(min_size=0, max_size=300)

passwords = st.text(min_size=1, max_size=50)


fuzz_settings = settings(
    max_examples=20,
    deadline=None,
    suppress_health_check=[
        HealthCheck.function_scoped_fixture,
    ],
)



@pytest.mark.django_db
@given(
    email=emails,
    password=passwords,
)
@fuzz_settings
def test_register_serializer_fuzz(email, password):
    data = {
        "email": email,
        "first_name": "test",
        "last_name": "user",
        "password": password,
        "confirm_password": password,
    }

    serializer = RegisterSerializer(data=data)

    assert serializer.is_valid() in (True, False)



@pytest.mark.django_db
@given(
    title=text,
    content=text,
    category=text,
    keywords=text,
)
@fuzz_settings
def test_article_create_serializer_fuzz(title, content, category, keywords):
    data = {
        "title": title,
        "content": content,
        "category": category,
        "keywords": keywords,
    }

    serializer = ArticleCreateSerializer(data=data)

    assert serializer.is_valid() in (True, False)


@pytest.mark.django_db
@given(
    text=text,
    rating=st.integers(min_value=1, max_value=5),
)
@fuzz_settings
def test_review_create_serializer_fuzz(text, rating):
    data = {
        "text": text,
        "rating": rating,
        "article": 1,
    }

    serializer = ReviewCreateSerializer(data=data)

    assert serializer.is_valid() in (True, False)