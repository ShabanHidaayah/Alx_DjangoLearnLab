from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # MUST HAVE THIS IMPORT
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('auth-token/', obtain_auth_token, name='api_token_auth'),  # MUST HAVE THIS LINE
    path('', include(router.urls)),
]
