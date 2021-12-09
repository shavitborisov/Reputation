from bot.bot import stream
from image.image_util import creator
import time

def convert_pic_and_send(bot, message):
	creator("bla.jpg", message).save("bla1.bmp")
	bot.send_pic("bla1.bmp")

def main():
	bot = stream()

	while True:
		messages = bot.read_pic_and_message("bla.jpg")
		time.sleep(0.4)

		for msg in messages.split("\n"):
			convert_pic_and_send(bot, msg)
			time.sleep(1)

		time.sleep(2)
		
		bot.stream_write("The name was successfully hidden")
		bot.stream_write("Always at your service, Mr. TrackerInjector")

if '__main__' == __name__:
    main()
