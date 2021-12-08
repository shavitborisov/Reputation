from bot.bot import stream

def main():
	bot = stream()

	while True:
		message = bot.read_pic_and_message("bla.jpg")

		# Insert message to bla.jpg here and then send new pic

		bot.send_pic("bla.jpg")
		bot.stream_write("Message hidden!")

if '__main__' == __name__:
    main()
