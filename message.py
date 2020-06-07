from twilio.rest import Client

account_id = 'Enter your account id here'
auth_token = 'Enter your auth token here'

client = Client(account_id,auth_token)

def sendMessage():
    message = client.messages.create(
        from_ = "whatsapp: + Enter twilio's whatsapp number here",
        body = "Ahoy world!",
        to = 'whatsapp: + Enter your whatsapp number here'
    )

    print(message.sid)