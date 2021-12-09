from bot.bot import stream
from image.image_util import creator
import time

def main():
	bot = stream()

	while True:
		message = bot.read_pic_and_message("bla.jpg")
		time.sleep(0.4)

		creator("bla.jpg", message).save("bla1.bmp")

		bot.send_pic("bla1.bmp")
		bot.stream_write("The name was successfully hidden")
		bot.stream_write("Always at your service, Mr. TrackerInjector")

if '__main__' == __name__:
    main()
