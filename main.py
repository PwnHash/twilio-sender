from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'

# Your Twilio phone number (in E.164 format, e.g. +15551234567)
from_number = 'YOUR_TWILIO_PHONE_NUMBER'

# The phone number you want to send the message to (in E.164 format)
to_number = 'RECIPIENT_PHONE_NUMBER'

# The custom sender ID you want to use (must be approved by Twilio)
custom_sender_id = 'YOUR_CUSTOM_SENDER_ID'

# The message you want to send
message = 'This is a test message'

# Create a Twilio client
client = Client(account_sid, auth_token)

# Send the message
message = client.messages.create(
    body=message,
    from_=custom_sender_id,
    to=to_number
)

print(f'Message sent with SID {message.sid}')
