from django.shortcuts import render

from .models import NewsPost
from .forms import NewsPostForm

# Create your views here.
def news_post_detail_view(request):
    obj = NewsPost.objects.get(id=1)
    context = {
        'object' : obj
    }
    return render(request, "NewsPost/detail.html", context)

def news_post_create_view(request):
    form = NewsPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = NewsPostForm()

    context = {
        'form' : form
    }

    return render(request, "NewsPost/create.html", context)