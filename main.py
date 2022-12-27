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

# The name of the .txt file containing the list of phone numbers (in E.164 format)
phone_numbers_file = 'phone_numbers.txt'

# Read the list of phone numbers from the .txt file
with open(phone_numbers_file, 'r') as f:
    phone_numbers = f.readlines()

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
