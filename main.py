from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'

# Your Twilio phone number (in E.164 format, e.g. +15551234567)
from_number = 'YOUR_TWILIO_PHONE_NUMBER'

# The custom sender ID you want to use (must be approved by Twilio)
custom_sender_id = 'YOUR_CUSTOM_SENDER_ID'

# The message you want to send
message = 'This is a test message'

# The list of phone numbers you want to send the message to (in E.164 format)
phone_numbers = ['RECIPIENT_PHONE_NUMBER_1', 'RECIPIENT_PHONE_NUMBER_2', ...]

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send the message to each phone number in the list
for phone_number in phone_numbers:
    message = client.messages.create(
        body=message,
        from_=custom_sender_id,
        to=phone_number
    )
    print(f'Message sent to {phone_number} with SID {message.sid}')
