# hackernews-django

## TODO

- [ ] jobs markdown field support
  - [ ] update model to support markdownfield
  - [ ] update form
  - [ ] update view
  - [link](https://www.youtube.com/watch?v=t61nTi0lIlk)
- [ ] improve forms (currently they look ugly)
- [ ] implement upvote system
- [ ] inside personal profile:
  - [ ] list: my news posts
  - [ ] list: my events
  - [ ] list: my jobs
  - [ ] list: upvoted
- reply should only work when logged in
- upvote button should do a post to increase count
- add link to other profiles to display posts,...

events

- [ ] add events model
- [ ] add events calendar
- [ ] [django-scheduler](https://github.com/llazzaro/django-scheduler)

accounts

- [ ] add account system
  - [x] login
  - [x] logout
  - [ ] register
  - [ ] add email confirmation
- [ ] profile page content
  - [ ] posted articles (news, events, jobs)
  - [ ] upvoted articles

upvotes

- [ ] add upvote system
- [ ] points [algorithm](https://medium.com/hacking-and-gonzo/how-hacker-news-ranking-algorithm-works-1d9b0cf2c08d)

comments

- [ ] comments model
- [ ] comments templating
- [ ] [Django-MPTT](https://django-mptt.readthedocs.io/en/latest/)

styling

- [x] re-add submit button (inside the profile page)
- [x] clicked links should be greyed out
- [x] add favicon
- [x] add time since posted ([timesince](https://docs.djangoproject.com/en/4.0/ref/templates/builtins/#timesince))
- [x] add header image
- [x] add basic css styling
- [x] allignment improvements
  - [x] width doesn't work when wide
- [x] filter links to only display domain
- [ ] if upvoted, `^` should be green



## Common Commands

Activate virtual environment: `source bin/activate`

Deactivate virtual environment: `deactivate`

Create admin: `python manage.py createsuperuser`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

## Code documentation

### NewsPost

> Each "News" post needs an entry in the database

```python
class NewsPost(models.Model):
    title   = models.CharField(max_length=100, blank=False)
    url     = models.URLField(max_length=300, blank=False)
    domain  = models.CharField(max_length=300, blank=False)
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
- **domain** `CharField`: A CharField, contains the (shortened) domain name of the posted link (used for the news homepage), set automatically when a new post is submitted.
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







