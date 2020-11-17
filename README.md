# HNPDFbot
### By [@sarrisv](https://github.com/sarrisv) and [@hashFactory](https://github.com/hashFactory)
Telegram bot to navigate and access HackerNews stories on mobile

@HNPDFbot

Use the bot to request top stories in the form of a numbered list.
The bot will (hopefully) send you a PDF of the linked item.

If you're wondering why this exists it's because some airlines offer free internet in-flight but only for messaging services. Telegram seems to work, including rich media like images and files. The idea is to use the free tier and still be able to navigate to my heart's content.

I only have a couple of days to do this before a transatlantic flight so crossing my fingers I get it done in time.

Hopefully complete navigation of pages. For example one could issue commands like "click Issues" and the bot would scan the page for links or buttons that contain that word and follow through.

Right now just getting a proof of concept to work.

Dependencies:
* [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) - To implement the telegram bot
* [HackerNewsAPI](https://github.com/karan/HackerNewsAPI) - Wrapper for the HN api (in python)
* [wkhtmltopdf](https://wkhtmltopdf.org/) - To render the pages to PDF
