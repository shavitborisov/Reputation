from bot.bot import stream
from image.image_util import investigator
import time

def main():
	bot = stream()

	while True:
		bot.read_pic_and_message("bla.jpg")
		time.sleep(0.4)

		name = investigator("bla.jpg")

		bot.stream_write("The guilty person's name is: " + name)
		bot.stream_write("Your humble servant, The Investigator")

if '__main__' == __name__:
    main()
