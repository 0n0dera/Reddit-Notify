from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

subreddits = {}

def home(**kwargs):
	ret = ''
	if len(kwargs) > 0:
		ret = '?' + '&'.join(['='.join((key,str(value))) for key,value in kwargs.items()])
	return HttpResponseRedirect('/notify' + ret)

def index(request):
	sr_dupe_error_msg = request.GET.get('sr_dupe_error_msg') or ''
	kw_dupe_error_msg = request.GET.get('kw_dupe_error_msg') or ''
	
	context = {
    	'title': 'Reddit Notify Tool',
    	'error_msgs': {
    		'sr_dupe_error_msg': sr_dupe_error_msg,
    		'kw_dupe_error_msg': kw_dupe_error_msg,
    	},
    	'subreddits': subreddits,
    }
	return render(request, 'notify/index.html', context)

def add_subreddit(request):
	new_sr = request.POST['subreddit']
	if new_sr in subreddits:
		error_msg = 'The subreddit ( ' + new_sr + ' ) is already tracked!'
		return home(sr_dupe_error_msg = error_msg)
	subreddits[new_sr] = []
	return home()

def del_subreddit(request, subreddit):
	del subreddits[subreddit]
	return home()


def add_keywords(request, subreddit):
	added_kws = request.POST['keywords'].split(',')
	new_kws = list(filter(lambda w: w not in subreddits[subreddit], added_kws))
	dupe_kws = list(filter(lambda w: w in subreddits[subreddit], added_kws))
	subreddits[subreddit].extend(new_kws)
	if len(dupe_kws) > 0:
		error_msg = 'The keywords: (' + ', '.join(dupe_kws) + ') are already tracked!'
		return home(kw_dupe_error_msg = error_msg)
	return home()

def del_keyword(request, subreddit, keyword):
	subreddits[subreddit].remove(keyword)
	return home()
