import telebot

def read_token(token_filename='token_tlg.txt'):
    with open(token_filename, 'r', encoding='utf-8') as token_file:
        token = token_file.read().strip()
        # print(token)
    return  token

def echo_bot():
    token = read_token()
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands='start')
    def start(m, res=False):
        bot.send_message(m.chat.id, 'Я на связи, напиши что-нибудь!')

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        bot.send_message(message.chat.id, 'Вы написали:  ' + message.text)

    bot.polling(none_stop=True, interval=0)


if __name__ == "__main__":
    echo_bot()
