from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from django.db.models import Q


from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin
from .forms import TweetModelForm
# Create your views here.

class RetweetView(View):
	def get(self, request,tweet_id, *args, **kwargs):
		tweet = get_object_or_404(Tweet, id=tweet_id)
		if request.user.is_authenticated():
			new_tweet = Tweet.objects.retweet(request.user, tweet)
			return HttpResponseRedirect("/")

		return HttpResponseRedirect(tweet.get_asbolute_url())


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	form_class 		= TweetModelForm
	template_name 	= 'create_view.html'
	# success_url 	= 'tweet:detail'
	login_url 		= '/admin/'


class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset 		= Tweet.objects.all()
	form_class 		= TweetModelForm
	template_name 	= 'update_view.html'
	# success_url 	= '/tweet/'


class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model 			= Tweet
	template_name 	= 'delete_confirm.html'



class TweetDetailView(DetailView):
	template_name 	= "detail_view.html"
	queryset 		= Tweet.objects.all()

	def get_object(self):
		id = self.kwargs.get("id")
		return Tweet.objects.get(id=id)

class TweetListView(ListView):
	template_name 	= "list_view.html"
	
	def get_queryset(self, *args, **kwargs):
		im_following = self.request.user.profile.get_following()
		qs = Tweet.objects.filter(user__in=im_following).order_by("-timestamp")
		query = self.request.GET.get("q", None)
		if query is not None:
			qs = qs.filter(
				Q(content__icontains=query) | 
				Q(user__username__icontains=query)
				)
		return qs

	def get_context_data(self, *args, **kwargs):
		context = super(TweetListView, self).get_context_data(*args, **kwargs)
		context["create_form"] = TweetModelForm()
		context["create_url"]  = reverse_lazy("tweet:create")
		return context


