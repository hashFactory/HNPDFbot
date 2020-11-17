
import json

class Story():
	def __init__(self, by, descendants, id, kids, score, time, title, type, url):
		self.by = by
		self.descendants = descendants
		self.id = id
		self.kids = kids
		self.score = score
		self.time = time
		self.title = title
		self.type = type
		self.url = url

	def __init__(self, jsoncontent):
		# do kids later
		self.by = jsoncontent['by']
		#self.descendants = jsoncontent['descendants']
		self.id = jsoncontent['id']
		self.score = jsoncontent['score']
		self.time = jsoncontent['time']
		self.title = jsoncontent['title']
		self.type = jsoncontent['type']
		self.url = jsoncontent['url']