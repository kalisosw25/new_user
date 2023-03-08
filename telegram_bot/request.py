# pip3 install pyTelegramBotAPI
import telebot


bot = telebot.TeleBot('1771955777:AAGCKYoXlJh1pgzrE8-2LOOr4GVhAmbzTco')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)


@bot.channel_post_handler(content_types = ['text'])#citySupportName
def process_step2(message):
    print("aaa")
    bot.forward_message(0000000000, message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Operator is here!")

bot.infinity_polling()