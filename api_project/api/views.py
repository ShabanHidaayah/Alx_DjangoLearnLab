from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    """
    API endpoint that allows books to be viewed.
    Read-only access for authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow read for anyone, write for authenticated

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed, created, updated, or deleted.
    Full CRUD operations require authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Require authentication for all operations
    
    def get_permissions(self):
        """
        Customize permissions based on action
        """
        if self.action == 'list' or self.action == 'retrieve':
            # Allow read-only access for list and retrieve actions
            return [permissions.IsAuthenticatedOrReadOnly()]
        # Require full authentication for create, update, delete
        return [permissions.IsAuthenticated()]
