## Displaying articles on pages

1. Update `news_view`:

```python
from NewsPost.models import NewsPost

def news_view(request, *args, **kwargs):
    obj = NewsPost.objects.all()
    context = {
        'object' : obj
    }
    return render(request, "news.html", context)
```

2. Update `news.html`:

```python
{% extends 'base.html' %}

{% block content %}
<h1> news </h1>

{% for each in objects %}
    <p>{{ each.title }}</p>
{% endfor %}

{% endblock %}
```

## Add submit button

### NewsPost

Add link to `news.html`:

```python
{% extends 'base.html' %}

{% block content %}
<h1> news </h1>

<a href="{% url "newscreate" %}">submit</a>

<ul>
{% for each in object %}
    <li>{{ each.title }}</li>
{% endfor %}
</ul>

{% endblock %}
```

### JobPost

1. Create `forms.py`

```python
from django import forms

from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = [
            'title',
            'description',
            'author',
        ]
```

2. Update `views.py`

```python
from .models import JobPost
from .forms import JobPostForm

def job_post_create_view(request):
    form = JobPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = JobPostForm()

    context = {
        'form' : form
    }

    return render(request, "JobPost/create.html", context)
```

3. Create a new template `JobPost/create.html`

```html
{% extends 'base.html' %}

{% block content %}

<form method="POST"> {% csrf_token %}
{{ form.as_p }}
<input type="submit" value="Save" />
</form>
{% endblock %}
```

4. Update `urls.py`

```python
from JobPost.views import job_post_create_view

urlpatterns = [
    path('', views.news_view, name='news'),
    path('newspost/', news_post_detail_view),
    path('newscreate/', news_post_create_view, name='newscreate'),
    path('jobcreate/', job_post_create_view, name='jobcreate'),
    ...
]
```

5. Add submit link to `jobs.html`

```html
{% extends 'base.html' %}

{% block content %}
<h1> jobs </h1>

<a href="{% url "jobcreate" %}">submit</a>

<ul>
{% for each in object %}
    <li>{{ each.title }}</li>
{% endfor %}
</ul>

{% endblock %}
```