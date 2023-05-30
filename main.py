import telebot
bot = telebot.TeleBot('6113123879:AAH3fw3D9oMdEgRabWaJHCSGLLLJB2HGBNo')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id , 'Hello😘')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id , 'Усі кажуть ' + message.text + ' а ти купи слона')
bot.polling()