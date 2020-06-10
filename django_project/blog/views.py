from django.shortcuts import render

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
        'posts': posts
    }
    print('Home Page!')
    return render(request, 'blog/home.html', context)


def about(request):
  return render(request, 'blog/about.html', {'title': 'About'})
