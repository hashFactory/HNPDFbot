#!/usr/bin/env python

from hn import HN

from datetime import datetime, time,  timedelta

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode

def topHN(update, context):
	update.message.reply_text("HI!!!!")
	print("Reached me")
	hn = HN()
	message_buffer = ""
	for s in hn.get_stories(story_type='', limit=10):
		message_buffer += str(i) + ". " + s.title + "\n"
	#result = pretty_print(stories)
	update.message.reply_text(result)

def pretty_print(stories):
	message_buffer = ""
	for i in range(0, len(stories)):
		message_buffer += str(i) + ". " + stories[i].title + "\n"
	return message_buffer