from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    context = {
    	'title': 'Reddit Notify Tool'
    }
    return render(request, 'notify/index.html', context)

def getinfo(request):
	try:
		subreddit = request.POST['subreddit']
		keywords = request.POST['keywords'].split(',')
	except (KeyError):
		return render(request, 'notify/error.html')
	else:
		context = {
			'title': 'Reddit Notify Tool',
			'subreddit': subreddit,
			'keywords': keywords,
		}
		return render(request,'notify/index.html',context)