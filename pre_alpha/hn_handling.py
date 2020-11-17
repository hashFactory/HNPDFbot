#!/usr/bin/env python

#from hn import HN
import json
import requests
import re

from story import Story

from datetime import datetime, time,  timedelta

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode

current_stories = []

def topHN(update, context):
	#update.message.reply_text("HI!!!!")
	print("Reached me")
	#essage_buffer = ""
	#result = pretty_print(stories)
	update.message.reply_markdown_v2(get_top_stories(5, 0))

def get_top_stories(number, offset):
	url = "https://hacker-news.firebaseio.com/v0/topstories.json"
	r = requests.get(url)
	story_ids = r.json()[offset:number+offset]
	stories = []
	for s in story_ids:
		url = "https://hacker-news.firebaseio.com/v0/item/" + str(s) + ".json"
		r = requests.get(url)
		stories.append(Story(r.json()))
	return pretty_print(stories, offset)

def pretty_print(stories, offset):
	message_buffer = ""
	for i in range(0, len(stories)):
		message_buffer += "*" + str(i+offset+1) + "*" + "\. " + re.escape(stories[i].title) + "\n"
	return message_buffer