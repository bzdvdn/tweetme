from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView

from .models import Tweet

from .forms import TweetModelForm
# Create your views here.


class TweetCreateView(CreateView):
	form_class = TweetModelForm
	template_name = 'create_view.html'
	success_url = '/tweet/create/'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(TweetCreateView, self).form_valid(form)

class TweetDetailView(DetailView):
	template_name = "detail_view.html"
	queryset = Tweet.objects.all()

	def get_object(self):
		id = self.kwargs.get("id")
		return Tweet.objects.get(id=id)

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