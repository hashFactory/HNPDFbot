import json, requests, re
from text_objects import Story, Comment
import pdfkit
import hashlib
import os.path

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
		message_buffer += "\n    *" + str(i+offset+1) + "*\. " + re.escape(stories[i].title) + "\n"
	message_buffer += "\nPage: " + str(page+1)
	return message_buffer

def sanitize_filename(filename):
	remove_punctuation_map = dict((ord(char), None) for char in '\/*?:"<>|')
	return filename.translate(remove_punctuation_map)

def get_pdf(url, title):
	filename = sanitize_filename(title)[:50] + ".pdf"
	path = "cache/" + filename
	if not os.path.isfile(path):
		pdfkit.from_url(url, path)
	return path

def get_html(url):
	r = requests.get(url)
	print(r.text)
	return ''
	