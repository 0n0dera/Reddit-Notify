import praw
import time
import threading
import webbrowser
from pprint import pprint

# Post class
class Post:
	def __init__(self, url):
		self.url = url

# global vars
posts = []
counter = 0
subreddits = list(map(str.lower,map(str.strip,input("Enter subreddits separated by commas (e.g. manga, anime): \n").split(','))))
keywords = list(map(str.lower,map(str.strip,input("Enter post keywords separated by commas (e.g. nisekoi, tower of god, re:zero): \n").split(','))))

# thread function
def get_posts():
	global posts
	global counter
	global subreddits
	global keywords
	# user agent name
	user_agent = "PRAW Manga Update Notifier 2.0: /u/blinkarchon"
	# create Reddit object
	r = praw.Reddit(user_agent=user_agent)

	visited_ids = set()

	while True:
		for sr in subreddits:
			new_posts = r.get_subreddit(sr).get_new(limit=10)
			for p in new_posts:
				if p.id not in visited_ids and any(keyword in p.title.lower() for keyword in keywords):
					visited_ids.add(p.id)
					posts.append(Post(p.url))
					print(counter+1, "- New post in r/" + sr, "at", time.strftime("%H:%M:%S"),": ",end="")
					print(p.title)
					counter += 1
		time.sleep(60)

def is_num(s):
	try:
		val = int(s)
		return True
	except ValueError:
		return False

# start thread
main_thread = threading.Thread(target=get_posts, args=[])
main_thread.daemon = True
main_thread.start()

time.sleep(1)

while True:
	index = input()
	if index == 'q':
		print("Bye!")
		break
	elif is_num(index) and int(index) <= counter and int(index) > 0:
		webbrowser.open(posts[int(index)-1].url)
	else:
		print("Invalid input.")
