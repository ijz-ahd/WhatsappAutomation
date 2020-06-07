# from twilio.rest import Client 
 
# account_sid = 'AC5afca0437ef5923b1e7f284004cdadac' 
# auth_token = '[AuthToken]' 
# client = Client(account_sid, auth_token) 
 
# message = client.messages.create( 
#                               from_='whatsapp:+14155238886',  
#                               body='Hello! This is an editable text message. You are free to change it and write whatever you like.',      
#                               to='whatsapp:+918825799779' 
#                           ) 
 
# print(message.sid)

from twilio.rest import Client

account_id = 'AC5afca0437ef5923b1e7f284004cdadac'
auth_token = '01ad200daa4e9957bfcb04da61264922'

client = Client(account_id,auth_token)

def sendMessage():
    message = client.messages.create(
        from_ = 'whatsapp:+14155238886',
        body = "Ahoy world!",
        to = 'whatsapp:+918825799779'
    )

    print(message.sid)