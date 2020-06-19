from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView)
from .models import Post


posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Past 1',
        'content': 'First Post Content',
        'date_posted': ' Auguset 27, 2018'
    },

    {
        'author': 'Jane Dow',
        'title': 'Blog Past 2',
        'content': 'Second Post Content',
        'date_posted': ' Auguset 28, 2018'
    }
]


# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    print('Home Page!')
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    


def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})
