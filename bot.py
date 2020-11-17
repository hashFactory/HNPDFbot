#!/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

import logging

from hn_interaction import *

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext, ConversationHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Global vars for convenience
page = 0
number = 5
offset = 0

# Stages
STORIES, COMMENTS = range(2)

# Story callback data
ONE, TWO, THREE, FOUR, FIVE, PREV, NEXT = range(7)

# Comment callback data
PARENT, CHILD, EXIT = range(3)

story_keyboard = [
    [
        InlineKeyboardButton("1", callback_data=str(ONE)),
        InlineKeyboardButton("2", callback_data=str(TWO)),
        InlineKeyboardButton("3", callback_data=str(THREE)),
        InlineKeyboardButton("4", callback_data=str(FOUR)),
        InlineKeyboardButton("5", callback_data=str(FIVE))
    ],
    [   
        InlineKeyboardButton("◀", callback_data=str(PREV)),
        InlineKeyboardButton("▶", callback_data=str(NEXT))
    ]
]

comment_keyboard = [
    [   
        InlineKeyboardButton("◀", callback_data=str(PREV)),
        InlineKeyboardButton("▶", callback_data=str(NEXT))
    ],
    [   
        InlineKeyboardButton("▲ Parent", callback_data=str(PARENT)),
        InlineKeyboardButton("▼ Child", callback_data=str(CHILD))
    ],
    [
        InlineKeyboardButton("Exit", callback_data=str(EXIT))
    ]
]

def start(update, context):
    update.message.reply_markdown_v2('Enjoy browsing Hacker News\!')
    
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Use /start to test this bot.")

def show_top_stories(update: Update, context: CallbackContext) -> int:
    # set keyboard variable
    reply_markup = InlineKeyboardMarkup(story_keyboard)

    # intialize page count
    context.user_data['page'] = 0

    # get intial stories
    stories = get_top_stories(context.user_data['page'], number, offset)
    context.user_data['stories'] = stories
    
    # format and send to user
    update.message.reply_markdown_v2(pretty_print_stories(context.user_data['page'], stories, offset), reply_markup=reply_markup)
    return STORIES

def show_prev_page(update: Update, context: CallbackContext) -> int:
    # answer query so it doesnt break and set keyboard variable
    query = update.callback_query
    query.answer()
    reply_markup = InlineKeyboardMarkup(story_keyboard)

    # update page count
    if context.user_data['page'] > 0:
        context.user_data['page'] = context.user_data['page'] - 1

    # update stories
    stories = get_top_stories(context.user_data['page'], number, offset)
    context.user_data['stories'] = stories

    # edit text with new stories
    query.edit_message_text(pretty_print_stories(context.user_data['page'], stories, offset), reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN_V2)
    return STORIES

def show_next_page(update: Update, context: CallbackContext) -> int:
    # answer query so it doesnt break and set keyboard variable
    query = update.callback_query
    query.answer()
    reply_markup = InlineKeyboardMarkup(story_keyboard)
    
    # update page count
    context.user_data['page'] = context.user_data['page'] + 1

    # update stories
    stories = get_top_stories(context.user_data['page'], number, offset)
    context.user_data['stories'] = stories

    # edit text with new stories
    query.edit_message_text(pretty_print_stories(context.user_data['page'], stories, offset), reply_markup=reply_markup, parse_mode=ParseMode.MARKDOWN_V2)
    return STORIES

def reply_post(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    reply_markup = InlineKeyboardMarkup(comment_keyboard)

    try: 
        # get pdf
        pdf = get_pdf(context.user_data['stories'][int(query.data)].url)
        query.answer()

        query.message.reply_document(open(pdf, 'rb'))

        #query.edit_message_text(context.user_data['stories'][int(query.data)])
        # send pdf to user
        # ???
        html = get_html(context.user_data['stories'][int(query.data)])
        # setup comment interface
        query.message.reply_markdown_v2('Comment: \n', reply_markup=reply_markup)
        return STORIES
    except:
        return STORIES

def show_prev_comment(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    return COMMENTS

def show_next_comment(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    return COMMENTS

def show_parent_comment(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    return COMMENTS

def show_child_comment(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()

    return COMMENTS

def read_secret():
    global secret
    with open("secret.key") as f:
        secret = "".join(f.read().split())
    return secret

def main():
    if not os.path.isdir("cache"):
        os.mkdir("cache")

    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(read_secret(), use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    updater.dispatcher.add_handler(ConversationHandler(
        entry_points = [CommandHandler('top', show_top_stories)],
        states = {
            STORIES: [
                CallbackQueryHandler(reply_post, pattern='^' + str(ONE) + '$'),
                CallbackQueryHandler(reply_post, pattern='^' + str(TWO) + '$'),
                CallbackQueryHandler(reply_post, pattern='^' + str(THREE) + '$'),
                CallbackQueryHandler(reply_post, pattern='^' + str(FOUR) + '$'),
                CallbackQueryHandler(reply_post, pattern='^' + str(FIVE) + '$'),
                CallbackQueryHandler(show_prev_page, pattern='^' + str(PREV) + '$'),
                CallbackQueryHandler(show_next_page, pattern='^' + str(NEXT) + '$'),
            ],
            COMMENTS: [
                CallbackQueryHandler(show_prev_comment, pattern='^' + str(PREV) + '$'),
                CallbackQueryHandler(show_next_comment, pattern='^' + str(NEXT) + '$'),
                CallbackQueryHandler(show_parent_comment, pattern='^' + str(PARENT) + '$'),
                CallbackQueryHandler(show_child_comment, pattern='^' + str(CHILD) + '$'),
                CallbackQueryHandler(show_top_stories, pattern='^' + str(EXIT) + '$')
            ],
        },
        fallbacks = [CommandHandler('top', show_top_stories)],
    ))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
