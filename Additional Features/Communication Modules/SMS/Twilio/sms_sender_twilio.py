from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACab2e11ac1e31bfcf526812013a5521f8'
auth_token = '3d3978488324a8a8c8000b37ae78acdd'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+14159806287',
         to='+918618824813'
     )

print(message.sid)