"""crega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from main.views import *

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^about/$', About.as_view(), name='about'),
    url(r'^products/product1/$', Product1.as_view(), name='product1'),
    url(r'^products/product2/$', Product2.as_view(), name='product2'),
    url(r'^products/product3/$', Product3.as_view(), name='product3'),
    url(r'^products/product4/$', Product4.as_view(), name='product4'),
    url(r'^services/service1/$', Service1.as_view(), name='service1'),
    url(r'^services/service2/$', Service2.as_view(), name='service2'),
    url(r'^enquiry/$', Enquiry.as_view(), name='enquiry'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^privacy/$', Privacy.as_view(), name='privacy'),
    url(r'^terms/$', Terms.as_view(), name='terms'),
    url(r'^news/$', AllNews.as_view(), name='news'),
    url(r'^news/(?P<pk>\d+)/$', SingleNews.as_view(), name='singlenews'),
    url(r'^thanks/$', Thanks.as_view(), name='thanks'),
]
