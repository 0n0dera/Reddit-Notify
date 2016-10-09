from django.conf.urls import url

from . import views

app_name = 'notify'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_subreddit/$', views.add_subreddit, name='add_subreddit'),
    url(r'^del_subreddit/(?P<subreddit>.*)$', views.del_subreddit, name='del_subreddit'),
    url(r'^add_keywords/(?P<subreddit>.*)$', views.add_keywords, name='add_keywords'),
    url(r'^del_keyword/(?P<subreddit>.*)/(?P<keyword>.*)$', views.del_keyword, name='del_keyword'),
]
