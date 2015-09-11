"""ScavengerRun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'timetracker_app.views.welcome', name='welcome'),
    url(r'cp/(\d+)/(\d+)/$', 'timetracker_app.views.cp', {'template_name': 'checkpoint.html'}, name='cp'),
    url(r'reports/$', 'timetracker_app.views.reports', {'template_name': 'reports.html'}, name='reports'),
    url(r'details/$', 'timetracker_app.views.details', {'template_name': 'details.html'}, name='details'),
]
