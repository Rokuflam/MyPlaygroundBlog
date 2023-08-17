from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Post
all_posts = []

def starting_page(request):
    latest_sorted_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/index.html', {
        'all_posts': latest_sorted_posts
    })

def posts(request):
    latest_sorted_posts = Post.objects.all().order_by('-date')
    return render(request, "blog/all-posts.html", {
        'all_posts': latest_sorted_posts
    })

def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        'post': identified_post,
        'post_tegs': identified_post.tags.all() 
        })