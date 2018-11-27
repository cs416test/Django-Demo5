"""CS416Django URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from mysite import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.test),
    url(r'^test2/', views.test2),
    url(r'^test3/', views.test3),

    url(r'^$', views.index, name='index'),
    url(r'^register/', views.viewRegister),
    url(r'^addUser/', views.addUser, name='addUser'),
    url(r'^deleteUser/', views.deleteUser, name='deleteUser'),
    #url(r'^addUser/(?P<firstName>.+)/(?P<lastName>.+)/(?P<age>\d+)/$', views.addUser, name='addUser'),

    #url(r'^todo/', views.toDo, name='todo'),

    #url(r'^accounts/', include('django.contrib.auth.urls')),

    #url(r'^user_example/', include('user_example.urls')),

    url(r'^simple_form/', include('simple_form.urls')),

    url(r'^simple_authentication/', include('simple_authentication.urls')),

    url(r'^simple_crud/', include('simple_CRUD.urls')),
]
