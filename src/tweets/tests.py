from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

# Create your tests here.
from .models import Tweet

User = get_user_model()

class TweetModelTestCase(TestCase):
	def setUp(self):
		some_random_user = User.objects.create(username="SOME_RANDOM_GUS_GUS")

	def test_tweet_item(self):
		obj = Tweet.objects.create(
			user= User.objects.first(),
			content="Some test content"
			)
		self.assertTrue(obj.content == "Some test content")
		self.assertTrue(obj.id == 1)
		absolute_url = reverse("tweet:detail", kwargs={"id":1})
		self.assertEqual(obj.get_absolute_url(), absolute_url)

	def test_tweet_url(self):
		obj = Tweet.objects.create(
			user= User.objects.first(),
			content="Some test content"
			)
		absolute_url = reverse("tweet:detail", kwargs={"id":obj.id})
		self.assertEqual(obj.get_absolute_url(), absolute_url)