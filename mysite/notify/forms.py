from django import forms

class AddSubredditForm(forms.Form):
	subreddit = forms.CharField(label='Subreddit', max_length=100)