def send_message(message):
	from twilio.rest import Client

	client = Client("Account SId", "Auth token")

	numbers = ["+916351816925", "+91xxxxxxxxxx",
			"+91xxxxxxxxxx", "+91xxxxxxxxxx"]
	names = ["Sarthak", "Hardeep", "Utsav", "Ahmed"]

	for i in range(4):
		m = ("Hello {} ".format(names[i]))+message
		client.messages.create(to=numbers[i],
							from_="number provided by the api",
							body=(m))
