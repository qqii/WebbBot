from telegram.ext import *
import mimetypes
import random
import time

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
    time.sleep(random.betavariate(8, 3) * 4)
    # random number of emojis
    bot.send_message(chat_id=update.message.chat_id, text="\U0001F602" * random.randint(2, 3))

def textimage(bot, update):
    print("{}({}): {}".format(update.message.from_user.username, 
                              update.message.date,
                              update.message.text))
    mt, _ = mimetypes.guess_type(update.message.text)
    if (mt and mt.startswith("image")) or (update.message.text.find("imgur.com") != -1):
        reply(bot, update)
        
def photo(bot, update):
    reply(bot, update)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    updater = Updater(key)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, textimage))
    dp.add_handler(MessageHandler(Filters.photo, photo))
    dp.add_error_handler(error)

    logger.info("Starting Webb Bot II")
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
