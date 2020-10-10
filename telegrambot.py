import requests as r, bs4, urllib.parse as u, telebot
from time import sleep

#Uncode is u.unquote(url)

def HTMLParser(url):
    # print(url)
    url = r.get(url)
    UrlHTML = bs4.BeautifulSoup(url.text, 'lxml')
    videoSource = UrlHTML.findAll('a', href=True)
    videoTag = [i for i in videoSource if 'mp4' in str(i)][0]
    videoTag = str(videoTag).split(';')[0]
    videoUrl = videoTag.split('src=')[1]
    return u.unquote(str(videoUrl))

def VideoUrl(url):
    try:
        if 'www' in url:
            url = url.replace('www', 'm')
            # print(url)
        elif '//f' in url:
            url = url.replace('//f', '//m.f')
            # print(url)
        elif 'm.' in url:
            pass
        else:
            return 'Revisa tu link todo culero'
        return HTMLParser(url)
    except IndexError:
        return 'Tu mamada no sirve'

if __name__ == "__main__":


    bot_token = '1131786920:AAE9-LP7rFGkFXR2iXlAhUv1QwAuIIalB78'
    bot = telebot.TeleBot(token=bot_token)


    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, 'ola gei')

    @bot.message_handler(func=lambda msg: msg.text is not None and '@Mmaguebot' in msg.text)
    def at_answer(message):
        fburl = message.text.split()[1]
        if 'http' not in fburl:
            fburl ='http://'+fburl
        bot.reply_to(message, VideoUrl(fburl))

    while True:
        try:
            bot.polling()
        except Exception:
            sleep(15)

