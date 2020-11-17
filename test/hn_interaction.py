import json, requests, re
from text_objects import Story, Comment
import pdfkit

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode

def get_top_stories(page, number, offset):
	url = "https://hacker-news.firebaseio.com/v0/topstories.json"
	r = requests.get(url)
	story_ids = r.json()[offset + page*number: offset + (page+1)*number]
	stories = []
	for s in story_ids:
		url = "https://hacker-news.firebaseio.com/v0/item/" + str(s) + ".json"
		r = requests.get(url)
		stories.append(Story(r.json()))
	return stories

def pretty_print_stories(page, stories, offset):
	message_buffer = "*Stories:* \n"
	for i in range(0, len(stories)):
		message_buffer += "\n    *" + str(i+offset+1) + "*" + "\. " + re.escape(stories[i].title) + "\n"
	message_buffer += "\nPage: " + str(page+1)
	return message_buffer

def get_pdf(url) -> bytes:
	return pdfkit.from_url(url, 'out.pdf')

def get_html(url) -> str:
	r = requests.get(url)
	print(r.text)
	return ''
	