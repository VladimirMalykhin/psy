"""psyho URL Configuration

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
from psyho_app.views import *
from psyho_app import views
from . import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', account_view),
    url(r'^chat/', chat_view),
    url(r'^book/', book_view),
    url(r'^homework/', homework_view),
        url(r'^music/', music_view),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^$',  views.LoginFormView.as_view()),
    url(r'^logout/$',  views.LogoutView.as_view()),
    url(r'^view/(?P<todo_id>\d+)/$',
        view_user, name='view'),
    url(r'^chat_clients/(?P<todo_id>\d+)/$',
        chat_user_view, name='chat_view'),
    url(r'^music_clients/(?P<todo_id>\d+)/$',
        music_user_view, name='music_view'),
    url(r'^music_delete/(?P<todo_id>\d+)/(?P<music_id>\d+)$',
        music_delete, name='music_delete'),
    url(r'^book_clients/(?P<todo_id>\d+)/$',
        book_user_view, name='book_view'),
    url(r'^homeworks_clients/(?P<todo_id>\d+)/$',
        homeworks_user_view, name='homeworks_view'),
    url(r'^one_homework/(?P<homework_id>\d+)/$',
        one_homework_view, name='one_homework_view'),
    url(r'^one_homework_users/(?P<todo_id>\d+)/(?P<homework_id>\d+)/$',
        one_homework_users_view, name='one_homework_users_view'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
