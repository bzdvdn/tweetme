from django.conf.urls import url

from django.views.generic.base import RedirectView 
from .views import UserDetailView, UserFollowView

urlpatterns = [
	# url(r'^create/$', TweetCreateView.as_view(), name='create'),
	# url(r'^search/$', TweetListView.as_view(), name="list"),
	url(r'^(?P<username>[\w.@+-]+)/follow/$', UserFollowView.as_view(), name="follow"),
	url(r'^(?P<username>[\w.@+-]+)/$', UserDetailView.as_view(), name="detail"),
	# url(r'^(?P<id>\d+)/update/$', TweetUpdateView.as_view(), name="update"),
	# url(r'^(?P<id>\d+)/delete/$', TweetDeleteView.as_view(), name="delete"),
	# url(r'^$', RedirectView.as_view(url="/")),
]