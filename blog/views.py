from django.conf.urls import patterns
from django.views.generic import ListView, CreateView

from blog.models import Post

# Create your views here.
class PostListView(ListView):
	model = Post
	template_name = 'blog/post_list.html'
	context_object_name = 'posts'

class PostCreateView(CreateView):
	model = Post
	template_name = 'blog/post_create.html'
	success_url = '/blog/'