#add sending images and videos capabilities
#add sending to multiple numbers capabilities
import os
from twilio.rest import Client

print('INPUT CREDENTIALS')
print('____________________')

ACCOUNT_SID = input('Type in your ACCOUNT_SID = ')
AUTH_TOKEN = input('Type in your AUTH_TOKEN = ')
print('Validating Credentials......')
client = Client(ACCOUNT_SID, AUTH_TOKEN)


#from hrhrhrh
message = input('Type in your message? ')
from_whatsapp_number='whatsapp:+14155238886'
to_whatsapp_number='whatsapp:+23490........'

client.messages.create(body='Ahoy world',from_=from_whatsapp_number, to=to_whatsapp_number)

print('Whatsapp message sent successfully!')
