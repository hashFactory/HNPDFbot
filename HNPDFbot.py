#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

import logging, random

#import pdfkit
from hn import HN
#from bs4 import BeautifulSoup

from datetime import time
import sys
import os
import signal

from hn_handling import *

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

updater = None

secret = ""

def read_secret():
    global secret
    with open("secret.key") as f:
        secret = "".join(f.read().split())

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Type \'/\' for list of functions')

def nope(update, context):
    """Echo the user message."""
    update.message.reply_text('Not a thing try again')

def error(update, context):
    """Log Errors caused by Updates."""
    global updater
    pid = os.getpid()
    os.kill(pid, signal.SIGTERM)
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    global updater
    # Create the Updater and pass it your bot's token.
    read_secret()
    print("|" + secret + "|")
    updater = Updater(secret, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("top", topHN))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, nope))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()
    print("Started polling...")

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
