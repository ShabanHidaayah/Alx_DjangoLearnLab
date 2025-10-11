from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            # Search by title
            title_results = Post.objects.filter(title__icontains=search_query)
            # Search by content
            content_results = Post.objects.filter(content__icontains=search_query)
            # Search by tags using tags_name_icontains
            tag_results = Post.objects.filter(tags_name_icontains=search_query)
            
            # Combine results
            queryset = title_results | content_results | tag_results
        return queryset
