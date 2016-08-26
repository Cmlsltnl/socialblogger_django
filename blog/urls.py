from django.conf.urls import url,include
from django.contrib import admin
from django.views.generic import ListView,DetailView
from .models import Post
from django.contrib.auth.decorators import login_required
from .views import BlogView,PostCreate,PostUpdate,PostDelete,PostListView,PostDetailView,MyPostListView,PostList
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   	# url(r'^$',ListView.as_view(queryset=Post.objects.all().order_by('-date')[:25],
								# template_name='blog/blog_home.html' )),
	# url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post,
											  # template_name = 'blog/blog_each.html')),
	url(r'^$',login_required(PostListView.as_view()),name='blog-list'),
	url(r'^(?P<pk>\d+)$',login_required(PostDetailView.as_view()),name='blog-detail') ,
	url(r'^blog$', login_required(BlogView.as_view()), name='blog-form'),
	url(r'^create$', login_required(PostCreate.as_view()), name='blog-create'),
	url(r'^update/(?P<pk>\d+)$', login_required(PostUpdate.as_view()), name='blog-update'),
	url(r'^delete/(?P<pk>\d+)$', login_required(PostDelete.as_view()), name='blog-update'),
	url(r'^my/$',login_required(MyPostListView.as_view()),name='my-list'),

	url(r'^json/$',login_required(PostList.as_view()),name='post-json')
	

]


urlpatterns = format_suffix_patterns(urlpatterns)

