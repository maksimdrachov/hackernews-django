from pipes import Template
from django.shortcuts import render

from django.http import HttpResponse

from NewsPost.models import NewsPost
from JobPost.models import JobPost

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

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
    obj = JobPost.objects.all()
    context = {
        'object' : obj
    }
    return render(request, "jobs.html", context)

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

class ProfileView(TemplateView, LoginRequiredMixin):
    template_name = 'accounts/profile.html'