from django.conf.urls import patterns, url

from blog.views import PostListView, PostCreateView

urlpatterns = patterns('',
	url(r'^$', PostListView.as_view(), name='post_list_view'),
	url(r'^create/$', PostCreateView.as_view(), name='post_create_view'),
)