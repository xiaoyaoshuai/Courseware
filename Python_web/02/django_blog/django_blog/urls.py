"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blogs import views as blog_views
from users import views as user_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index/$', blog_views.Index.as_view(), name='index'),
    url(r'^blog_list/$', blog_views.Bloglist.as_view(), name='bloglist'),
    url(r'^tags_list/(?P<tid>\d+)/$', blog_views.Bloglist.as_view(), name='taglist'),
    url(r'^search/$', blog_views.search, name='search'),
    url(r'^blog_detail/(?P<pid>\d+)/$', blog_views.blog_detail, name='blog_detail'),
    url(r'^login/$', user_views.LoginView.as_view(), name='login'),
    url(r'^register/$', user_views.RegisterView.as_view(), name='register'),
    url(r'^logout/$', user_views.LogoutView.as_view(), name='logout'),
    url(r'^active/(?P<active_code>[a-zA-Z0-9]+)', user_views.ActiveView.as_view(), name='active'),
]
