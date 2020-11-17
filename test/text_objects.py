
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
		self.by = jsoncontent['by']
		if 'descendants' in jsoncontent: 
			self.descendants = jsoncontent['descendants']
		self.id = jsoncontent['id']
		if 'kids' in jsoncontent: 
			self.kids = jsoncontent['kids']
		self.score = jsoncontent['score']
		self.time = jsoncontent['time']
		self.title = jsoncontent['title']
		self.type = jsoncontent['type']
		self.url = jsoncontent['url']

class Comment():
	def __init__(self, by, id, kids, parent, text, time, type):
		self.by = by
		self.id = id
		self.kids = kids
		self.parent = parent
		self.text = text
		self.time = time
		self.type = type

	def __init__(self, jsoncontent):
		self.by = jsoncontent['by']
		self.id = jsoncontent['id']
		if 'kids' in jsoncontent: 
			self.kids = jsoncontent['kids']
		if 'parent' in jsoncontent:
			self.parent = jsoncontent['parent']
		if 'text' in jsoncontent:
			self.text = jsoncontent['text']
		self.time = jsoncontent['time']
		self.type = jsoncontent['type']