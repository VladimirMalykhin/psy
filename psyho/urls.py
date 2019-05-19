from django.conf.urls import url
from django.contrib import admin
from psyho_app.views import *
from psyho_app import views
from . import settings
from psyho_app.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', account_view),
    url(r'^chat/', chat_view),
    url(r'^blog/', blog_view),
    url(r'^book/', book_view),
    url(r'^contacts/',contacts),
    url(r'^homework/', homework_view),
    url(r'^anketa/', anketa_view),
        url(r'^music/', music_view),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^auth/$',  views.LoginFormView.as_view()),
    url(r'^$', main_views),
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
    
    url(r'^news/(?P<id>\d+)/(?P<title>[-\w]+)/$', product_detail, name='BlogDetail'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
