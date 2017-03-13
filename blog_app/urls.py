from django.conf.urls import url
import views

urlpatterns = [

    url(r'^$', views.post_list, name='post_list'),
    url(r'^posts/(?P<id>\d+)/$',views.post_details, name='postdetail'),
    url(r'^posts/new/$', views.create_post, name='new_post'),
     url(r'^posts/(?P<id>\d+)/edit$', views.edit_post,name='edit'),
]