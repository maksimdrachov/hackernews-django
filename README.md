# hackernews-django

## Common Commands

Activate virtual environment: `source bin/activate`

Deactivate virtual environment: `deactivate`

Create admin: `python manage.py createsuperuser`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

## Models

### NewsPost

> Each "News" post needs an entry in the database

```python
class NewsPost(models.Model):
    title   = models.CharField(max_length=100, blank=False)
    url     = models.URLField(max_length=300, blank=False)
    author  = models.CharField(max_length=20, blank=False)
    time    = models.DateTimeField(auto_now_add=True, blank=False)
    votes   = models.IntegerField(default=0, blank=False)
```

- **title** `CharField`: A string field, contains the post's title
  - `max_length=100`: sets the max length of the title to 100 characters
  - `blank=False`: the field is not allowed to be blank/empty
- **url** `URLField`: A CharField for a URL, validated by URLValidator
  - `max_length=300`: sets the max length
  - `blank=False`: the field is not allowed to be blank/empty
- **author** `CharField`
  - contains the author username of the post (_should be changed to the username of the poster_)
- **time** `DateTimeField`
  - timestamp when the post was made (date + time)
  - `settings.py`: `TIME_ZONE = 'Europe/Tallinn'`
    - sets correct timezone
- **votes** `IntegerField`
  - number of upvotes, starts at 0

### JobPost

> Each "Job" post needs an entry in the database

`python manage.py startapp JobPost`

`models.py`:

```python
class JobPost(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    author = models.CharField(max_length=20, blank=False)
    time = models.DateTimeField(auto_now_add=True, blank=False)
```

`settings.py`:

```py
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # third party

    # own
    'JobPost',
]
```

`admin.py`:

```python
from .models import JobPost

admin.site.register(JobPost)
```

`python manage.py makemigrations`

`python manage.py migrate`

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



## TODO

- [x] show all news articles on home page
- [x] add submit button to news
- [ ] add detail view to links in news
- [x] show all job postings on home page
- [x] add submit button to jobs
- [ ] add detail view to links in jobs

- [ ] add events calendar
- [ ] add account system
  - [x] login
  - [x] logout
  - [ ] register
- [ ] add upvote system

- [ ] improve styling
  - [ ] re-add submit button (inside the profile page)
- [ ] add header image