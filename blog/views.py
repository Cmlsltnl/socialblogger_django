from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

from django.db.models import Q
# @login_required(login_url="login/")
class PostListView(ListView):

    template_name = 'blog/blog_home.html'

    def get_queryset(self):
        querylist = Post.objects.all()
        query = self.request.GET.get("q")
        
        if query:
            querylist = querylist.filter(Q(title__icontains=query) |
                                         Q(body__icontains=query) |
                                         Q(user__username__icontains=query)).order_by('-created_on')
            return querylist
        return Post.objects.all().order_by('-created_on')[:25]
   

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog_each.html'



class BlogView(FormView):
    template_name = 'blog/blog.html'
    
    success_url = '/blog/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super(BlogView, self).form_valid(form)


class PostCreate(CreateView):
    model = Post
    form_class =  PostForm
    success_url = '/blog/'
    title = 'Add Post'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(UpdateView):
    model = Post
    form_class =  PostForm
    template_name_suffix = '_update_form'
    title = 'Update Post'
    success_url = '/blog/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostUpdate, self).form_valid(form)


class PostDelete(DeleteView):
    model = Post
    # success_url = reverse_lazy('post-list')
    success_url = '/blog/'


class MyPostListView(ListView):
    template_name = 'blog/blog_home.html'

    def get_queryset(self):
        return Post.objects.all().filter(user=self.request.user)









# from myapp.forms import ContactForm
# from django.views.generic.edit import FormView

# class ContactView(FormView):
#     template_name = 'contact.html'
#     form_class = ContactForm
#     success_url = '/thanks/'

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super(ContactView, self).form_valid(form)



#createview

# from django.views.generic.edit import CreateView
# from myapp.models import Author

# class AuthorCreate(CreateView):
#     model = Author
#     fields = ['name']






#updateview

# from django.views.generic.edit import UpdateView
# from myapp.models import Author

# class AuthorUpdate(UpdateView):
#     model = Author
#     fields = ['name']
#     template_name_suffix = '_update_form'









#deleteview

# from django.views.generic.edit import DeleteView
# from django.core.urlresolvers import reverse_lazy
# from myapp.models import Author

# class AuthorDelete(DeleteView):
#     model = Author
#     success_url = reverse_lazy('author-list')


















