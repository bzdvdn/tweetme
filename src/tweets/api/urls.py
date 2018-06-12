from django.conf.urls import url
from .views import (
	TweetCreateAPIView,
	TweetListAPIView,
	RetweetAPIView,
	LikeToggleAPIView,
	TweetDetailAPIView,
	)

urlpatterns = [
	url(r'^$', TweetListAPIView.as_view(), name='list'), #/api/tweet/
	url(r'create/$', TweetCreateAPIView.as_view(), name='create'), #/api/tweet/
	url(r'^(?P<pk>\d+)/$', TweetDetailAPIView.as_view(), name="detail"),
	url(r'^(?P<tweet_id>\d+)/retweet/$', RetweetAPIView.as_view(), name="retweet"),
	url(r'^(?P<tweet_id>\d+)/like/$', LikeToggleAPIView.as_view(), name="like"),
]