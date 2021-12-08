from bot.bot import stream
import time

def main():
	bot = stream()

	while True:
		bot.read_pic_and_message("bla.jpg")
		time.sleep(0.4)

		# Here extract message from jpg and send it

		bot.stream_write("The guilty person's name is: " + "Kotick")
		bot.stream_write("Your humble servant, The Investigator")

if '__main__' == __name__:
    main()
