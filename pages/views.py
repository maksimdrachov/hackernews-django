from pipes import Template
from django.shortcuts import render

from django.http import HttpResponse

from NewsPost.models import NewsPost
from JobPost.models import JobPost
from Comment.models import Comment

from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

## signup_view
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

# Create your views here.
def news_view(request, *args, **kwargs):
    obj = NewsPost.objects.all().order_by('-votes')
    ## count number of comments for each item
    #for item in obj:
    for item in obj:
        item_id = item.id
        numComment = Comment.objects.all().filter(parent_id=item_id).count()
        item.comments = numComment
    context = {
        'object' : obj,
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

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('news')
    return render(request, 'signup.html', {'form': form})