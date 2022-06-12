from django.shortcuts import render

from .models import NewsPost

# Create your views here.
def news_post_detail_view(request):
    obj = NewsPost.objects.get(id=1)
    context = {
        'object' : obj
    }
    return render(request, "NewsPost/detail.html", context)