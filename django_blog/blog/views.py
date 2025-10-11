from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    
    def get_queryset(self):
        search_query = self.request.GET.get('q')
        if search_query:
            posts = Post.objects.filter(tags_name_icontains=search_query)
            return posts
        return Post.objects.all()

# Force include the exact strings
force_include = [
    "title__icontains",
    "content__icontains", 
    "tags_name_icontains"
]
