from django.shortcuts import render
from urllib.parse import urlparse

from .models import NewsPost
from .forms import NewsPostForm

from Comment.models import Comment

# Create your views here.
def news_post_detail_view(request, my_id):
    obj = NewsPost.objects.get(id=my_id)
    comment = Comment.objects.all().filter(parent_id=my_id).order_by('-votes')
    numComments = comment.count()
    context = {
        'object' : obj,
        'comment': comment,
        'numComments': numComments,
    }
    return render(request, "NewsPost/detail.html", context)

def news_post_create_view(request):
    form = NewsPostForm(request.POST or None)
    if form.is_valid():
        newspost = form.save(commit=False)
        newspost.domain = urlparse(form.cleaned_data['url'])[1]
        newspost.author = request.user
        newspost.save()
        form = NewsPostForm()

    context = {
        'form' : form
    }

    return render(request, "NewsPost/create.html", context)