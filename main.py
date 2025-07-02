
import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, "Бот работает!")

bot.infinity_polling()
