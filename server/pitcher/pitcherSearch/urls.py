from django.urls import path, include
from .views import (
    ProductSearch,
)

urlpatterns = [
    path('search', ProductSearch.as_view()),
]