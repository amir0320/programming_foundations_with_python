from twilio.rest import TwilioRestClient

account_sid = "AC9857380105a99913c74bcf8d49f29786"
auth_token = "7e57978aa939bad9de82343a67308513"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body = "I'm sending this message from my computer :)  -Amir", # Replace with your desired message
    to = "",	# fill in your phone number
    from_ = "") # fill in your twilio number

print message.sid
