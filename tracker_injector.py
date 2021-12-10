from bot.bot import stream
from image.image_util import creator
import time

def convert_pic_and_send(bot, message):
	creator("bla.jpg", message).save("bla1.bmp")
	bot.send_pic("bla1.bmp", message)

def main():
	bot = stream()

	while True:
		messages = bot.read_pic_and_message("bla.jpg")
		time.sleep(0.4)

		for msg in messages.split("\n"):
			if not msg:
				continue

			convert_pic_and_send(bot, msg)
			time.sleep(0.5)

		time.sleep(2)
		
		bot.stream_write("The information was successfully hidden")
		bot.stream_write("Always at your service, Mr. TrackerInjector")

if '__main__' == __name__:
    main()
