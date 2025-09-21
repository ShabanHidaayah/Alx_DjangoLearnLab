from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # IMPORT FOR TOKEN AUTH
from .views import BookList, BookViewSet

# Create a router and register our ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Token authentication endpoint - USES DRF'S BUILT-IN obtain_auth_token VIEW
    path('auth-token/', obtain_auth_token, name='api_token_auth'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]
