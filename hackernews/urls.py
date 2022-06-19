"""hackernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages import views
from NewsPost.views import news_post_detail_view, news_post_create_view
from JobPost.views import job_post_create_view

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.news_view, name='news'),
    path('newspost/', news_post_detail_view),
    path('newscreate/', news_post_create_view, name='newscreate'),
    path('events/', views.events_view, name='events'),
    path('jobs/', views.jobs_view, name='jobs'),
    path('jobcreate', job_post_create_view, name='jobcreate'),
    path('about/', views.about_view, name='about'),
    path('admin/', admin.site.urls),

    #accounts
    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    path('accounts/logout', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile', views.ProfileView.as_view(), name="profile"),
]
