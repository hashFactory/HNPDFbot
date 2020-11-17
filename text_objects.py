
import json

class Story():
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