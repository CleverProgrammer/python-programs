from twilio import rest 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC22349ef1a076902f0312e4618de465b5"
auth_token  = "7afa0932a5640830d861adc2bcca5a27"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="http://www.il-chess.org/index.php/tournaments-all/details/1536-glenwood-chess-club-quad-tournament",
    to="+12247257844",    # Replace with your phone number
    from_="+12245325043") # Replace with your Twilio number
print message.sid
