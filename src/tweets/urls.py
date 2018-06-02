from django.conf.urls import url

from django.views.generic.base import RedirectView 
from .views import TweetDetailView, TweetListView, TweetCreateView, TweetUpdateView, TweetDeleteView

urlpatterns = [
	url(r'^create/$', TweetCreateView.as_view(), name='create'),
	url(r'^search/$', TweetListView.as_view(), name="list"),
	url(r'^(?P<id>\d+)/$', TweetDetailView.as_view(), name="detail"),
	url(r'^(?P<id>\d+)/update/$', TweetUpdateView.as_view(), name="update"),
	url(r'^(?P<id>\d+)/delete/$', TweetDeleteView.as_view(), name="delete"),
	url(r'^$', RedirectView.as_view(url="/")),
]