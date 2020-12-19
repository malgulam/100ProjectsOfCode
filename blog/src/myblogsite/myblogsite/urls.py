"""myblogsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
import sys
sys.path.append('..')
from blog.views import home_view, signup, login, blog_view

urlpatterns = [
    path('', home_view, name='home'),
    url(r'^signup/$', signup, name='signup'),
    url(f'^login$', login, name='login'),
    url(f'^blog_view/$', blog_view, name="blog_view"),
    path('admin/', admin.site.urls),
]
