import requests as r, bs4, urllib.parse as u, telebot
from time import sleep

def HTMLParser(url):
	UrlHTML = bs4.BeautifulSoup(r.get(url).text, 'lxml')
	videoUrl = str([i for i in UrlHTML.findAll('a', href=True) if 'mp4' in str(i)][0]).split(';')[0].split('src=')[1]
	return u.unquote(str(videoUrl))

def VideoUrl(url):
	try:
		url = 'https://m.facebook.com/' + url.split('.com', 1)[1] if 'facebook' in url else 'https://m.facebook.com/' + url
		return HTMLParser(url) #return (f'Your Video URL is: {HTMLParser(url)}')
	except Exception as e:
		return 'An error has occurred, please contact the script creator.'

if __name__ == "__main__":


	bot_token = '<BOT_TOKEN>'
	bot = telebot.TeleBot(token=bot_token)


	@bot.message_handler(commands=['start'])
	def send_welcome(message):
		bot.reply_to(message, 'Hello Test')
	@bot.message_handler(func=lambda msg: msg.text is not None and '@BotName' in msg.text)
	def at_answer(message):
		fburl = message.text.split()[1]
		bot.send_video(message.chat.id, VideoUrl(fburl), supports_streaming=True, reply_to_message_id=message.message_id)
	while True:
		try:
			bot.polling()
		except Exception:
			sleep(15)