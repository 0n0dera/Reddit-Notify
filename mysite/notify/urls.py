from django.conf.urls import url

from . import views

app_name = 'notify'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^addsubreddit/$', views.addsubreddit, name='addsubreddit'),
    url(r'^addkeywords/(?P<subreddit>.*)$', views.addkeywords, name='addkeywords'),
]
