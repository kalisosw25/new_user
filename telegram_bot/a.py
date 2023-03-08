import telebot

bot = telebot.TeleBot('1771955777:AAGCKYoXlJh1pgzrE8-2LOOr4GVhAmbzTco')

# # Replace GROUP_CHAT_ID with the ID of your private group chat
# chat_id = '-100894055134'
chat_id = -1001842906958
# # Send a message to the group chat
bot.send_message(chat_id, 'Hello, this is a message from the bot!')
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	# bot.send_message(message.chat.id, message.chat.type)
	
    sms = message
    print(sms)

	
bot.infinity_polling()