from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    context = {
        'Post': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact'})