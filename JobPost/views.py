from django.shortcuts import render

from .models import JobPost
from .forms import JobPostForm

# Create your views here.

def job_post_detail_view(request, my_id):
    obj = JobPost.objects.get(id=my_id)
    context = {
        'object' : obj
    }
    return render(request, "JobPost/detail.html", context)

def job_post_create_view(request):
    form = JobPostForm(request.POST or None)
    if form.is_valid():
        jobpost = form.save(commit=False)
        jobpost.author = request.user
        jobpost.save()
        form = JobPostForm()

    context = {
        'form' : form
    }

    return render(request, "JobPost/create.html", context)