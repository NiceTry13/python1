import telebot

bot = telebot.TeleBot("5567541172:AAEKdSoGWruW7S3URJoRT9RPOYPncqJ1i0k")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	bot.reply_to(message, message.text)


bot.infinity_polling( none_stop = True)