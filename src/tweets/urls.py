from django.conf.urls import url
from .views import TweetDetailView, TweetListView, TweetCreateView

urlpatterns = [
	url(r'^create/$', TweetCreateView.as_view(), name='create'),
	url(r'^$', TweetListView.as_view(), name="list"),
	url(r'^(?P<id>\d+)/$', TweetDetailView.as_view(), name="detail"),
]