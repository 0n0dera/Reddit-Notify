from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

subreddits = {}

def index(request):
    context = {
    	'title': 'Reddit Notify Tool',
    	'subreddits': subreddits,
    }
    return render(request, 'notify/index.html', context)

def addsubreddit(request):
	try:
		subreddits[request.POST['subreddit']] = []
	except (KeyError):
		return render(request, 'notify/error.html')
	else:
		return HttpResponseRedirect('/notify')

def addkeywords(request, subreddit):
	subreddits[subreddit].extend(request.POST['keywords'].split(','))
	return HttpResponseRedirect('/notify')