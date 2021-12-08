from bot.bot import stream
import time

def main():
	bot = stream()

	while True:
		message = bot.read_pic_and_message("bla.jpg")
		time.sleep(0.4)

		# Insert message to bla.jpg here and then send new pic

		bot.send_pic("bla.jpg")
		bot.stream_write("The name was successfully hidden")
		bot.stream_write("Always at your service, Mr. TrackerInjector")

if '__main__' == __name__:
    main()
