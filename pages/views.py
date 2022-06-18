from django.shortcuts import render

from django.http import HttpResponse

from NewsPost.models import NewsPost

# Create your views here.
def news_view(request, *args, **kwargs):
    obj = NewsPost.objects.all()
    context = {
        'object' : obj
    }
    return render(request, "news.html", context)

def events_view(request, *args, **kwargs):
    return render(request, "events.html", {})

def jobs_view(request, *args, **kwargs):
    return render(request, "jobs.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})