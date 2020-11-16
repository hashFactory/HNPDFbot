#!/usr/bin/env python

from datetime import datetime, time,  timedelta

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode

def topHN(update, context):
	hn = HN()
	hn.get_stories(story_type='', limit=10)

def pretty_print(stories):
	message_buffer = ""
	for i in range(0, len(stories)):
		mesage_buffer += str(i) + ". " + stories[i].title + "\n"
	