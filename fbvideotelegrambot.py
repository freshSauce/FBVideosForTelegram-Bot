import requests as r, bs4, urllib.parse as u, telebot
from time import sleep

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
            return 'Your link doesn\'t work'
        return HTMLParser(url)
    except:
        return 'An error has occured, please contact the bot creator.'

if __name__ == "__main__":


    bot_token = '<BOT_TOKEN>'
    bot = telebot.TeleBot(token=bot_token)


    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, 'TEST MESSAGE')

    @bot.message_handler(func=lambda msg: msg.text is not None and '@BotName' in msg.text)
    def at_answer(message):
        fburl = message.text.split()[1]
        if 'http' not in fburl:
            fburl ='http://'+fburl
        bot.reply_to(message, VideoUrl(fburl)) #comment this line to send the video instead of link.
        #If you want to send the just the video without link use this:
        #bot.send_video(message.chat.id, VideoUrl(fburl), supports_streaming=True, reply_to_message_id=message.message_id)

    while True:
        try:
            bot.polling()
        except Exception:
            sleep(15)

