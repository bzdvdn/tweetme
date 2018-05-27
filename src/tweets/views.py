from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Tweet
# Create your views here.


class TweetDetailView(DetailView):
	template_name = "detail_view.html"
	queryset = Tweet.objects.all()

	def get_object(self):
		return Tweet.objects.get(id=1)

class TweetListView(ListView):
	template_name = "list_view.html"
	queryset = Tweet.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		# print(context)
		# context["another_list"] = Tweet.objects.all()
		return context



# def tweet_detail_view(request, id=1):
# 	tweet = Tweet.objects.get(id=id)
# 	return render(request, "tweets/detail_view.html",
# 		{
# 			"tweet": tweet
# 		})


# def tweet_list_view(request, id=1):
# 	tweets = Tweet.objects.all()
# 	return render(request, "tweets/list_view.html",
# 		{
# 			"tweets": tweets,
		# })  