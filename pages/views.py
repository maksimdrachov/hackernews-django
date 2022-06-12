from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def news_view(request, *args, **kwargs):
    return render(request, "news.html", {})

def events_view(request, *args, **kwargs):
    return render(request, "events.html", {})

def jobs_view(request, *args, **kwargs):
    return render(request, "jobs.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})