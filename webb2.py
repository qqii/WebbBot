from telegram.ext import *
import mimetypes
import random
import time
import datetime
from collections import defaultdict

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger("Bot")

with open("key.txt", "r") as f:
    key = f.read().strip();

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

def reply(bot, update):
    # http://homepage.divms.uiowa.edu/~mbognar/applets/beta.html
    # peak near 3, human delay time
    time.sleep(random.betavariate(7, 3) * 4)
    # random number of emojis
    r = random.randint(0, 100)
    if r < 75:
        bot.send_message(chat_id=update.message.chat_id, text="\U0001F602" * random.randint(2, 3))
    elif r < 90:
        bot.send_message(chat_id=update.message.chat_id, text="Snazzy")
    elif r < 95:
        bot.send_message(chat_id=update.message.chat_id, text="That's pretty snazzy")
    elif r < 99:
        bot.send_message(chat_id=update.message.chat_id, text="Snazzy :)")
    else:
        bot.send_message(chat_id=update.message.chat_id, text="\U0001F602" * random.randint(2, 3))
        time.sleep(random.betavariate(7, 3) * 2)
        bot.send_message(chat_id=update.message.chat_id, text="I agree")
        time.sleep(random.betavariate(7, 3) * 2)
        bot.send_message(chat_id=update.message.chat_id, text="So true")
        time.sleep(random.betavariate(7, 3) * 2)
        bot.send_message(chat_id=update.message.chat_id, text="That's pretty snazzy")

def text(bot, update):
    # print("{}({}): {}".format(update.message.from_user.username,
                            #   update.message.date,
                            #   update.message.text))
    mt, _ = mimetypes.guess_type(update.message.text)
    if (mt and mt.startswith("image")) or (update.message.text.find("imgur.com") != -1):
        reply(bot, update)

def photo(bot, update):
    reply(bot, update)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

lm = defaultdict(lambda: datetime.datetime(2017, 5, 17))

def message(bot, update):
    global lm

    if (update.message.date - lm[update.message.chat.id] > datetime.timedelta(0, 5)):
        if update.message.photo:
            photo(bot, update)
        else:
            text(bot, update)
    lm[update.message.chat.id] = update.message.date

def main():
    updater = Updater(key)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_error_handler(error)
    dp.add_handler(MessageHandler(Filters.all, message))

    logger.info("Starting...")
    updater.start_polling()
    updater.idle()
    logger.info("Stopping...")


if __name__ == '__main__':
    main()
