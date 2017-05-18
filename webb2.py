import logging
from telegram.ext import *

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

with open("key.txt", "r") as f:
    key = f.read().strip();
    
updater = Updater(token=key)
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()

print("Running bot, press enter to stop...")
input()
print("Bot stopping...")
updater.stop()
print("Bot stopped.")
