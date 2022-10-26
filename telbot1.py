import telebot
from config import keys, TOKEN
from extensions import ConvetionExeption, CryptoConverter

bot = telebot.TeleBot (TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_help(message):
    bot.send_message(message.chat.id, f"Здравствуй {message.chat.username}."
                                      f"Чтобы начать работу введите комманды боту \n <Название валюты с маленькой буквы>, <В какую валюту перевод>, <кол-во переводимой валюты>. "
                                      f"Чтобы узнать какие валюты конвертируются введите '/values'" )

@bot.message_handler(commands=['values'])
def values (message: telebot.types.Message):
    text = 'Доступные валюты'
    for key in keys.keys():
        text ='\n'.join((text, key))
    bot.reply_to(message,text)

@bot.message_handler(content_types=['text',])
def convert (message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvetionExeption('Слишком много параметров.')
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvetionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Неудалось обработать комманду\n{e})')
    else:
        text = f'цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)
bot.polling(none_stop=True)