from constants import API_KEY
from telegram import Update, Bot
from telegram.ext import Updater, CallbackContext, CommandHandler
import random
# A list of quotes by Andrew Tate
quotes = [
    "The only way to succeed is to work harder than anyone else.",
    "There are no shortcuts to success.",
    "The only way to achieve greatness is to never give up.",
    "If you want to succeed, you have to be willing to put in the hard work."
]

def start(update: Update, context: CallbackContext):
    update.message.reply_text("It's TopG here to inspire you with words of truth and wisdom")

def topG(update: Update, context: CallbackContext):
    response= quotes[random.randint(0,len(quotes)-1)]
    update.message.reply_text(response)
    Bot.send_animation()

def error(update: Update, context: CallbackContext):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(token=API_KEY, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("topG", topG))
    dispatcher.add_error_handler(error)

    updater.start_polling(5)
    updater.idle()


if __name__ == '__main__':
    print("Bot Started...")
    main()
