from django.shortcuts import render
from .models import*
# Create your views here.
def view_post(request, id):
    post_obj = Posts.objects.get(pk=id)
    comments = Comment.objects.filter(post=post_obj)
    
    context = {
        'comments': comments,
        'post_obj': post_obj
    }

    return render(request, 'app1/main.html', context)