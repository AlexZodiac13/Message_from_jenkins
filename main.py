import telebot
bot = telebot.TeleBot('745192957:AAE1I3Mi-p0P0mdOj1sQoTht9qneP01BAxk')
commit = open("commit.txt",'r').read()
bot.send_message(410461386, commit)
@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привввет')
    print(message.chat.id)
