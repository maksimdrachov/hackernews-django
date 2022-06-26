from django.shortcuts import render

from .models import Comment
from .forms import CommentForm

# Create your views here.

def comment_create_view(request, my_id):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.parent_id = my_id
        comment.save()
        form = CommentForm()
    
    context = {
        'form' : form
    }

    return render(request, "Comment/create.html", context)