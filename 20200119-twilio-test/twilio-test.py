from twilio.rest import Client

account_sid = 'ACc0d5a9ce22abc91c42405dee4b0cfefd'
auth_token = '39c9f9f12d01ad268d54c1ccf90c47be'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="xaingfashenmejiufashenme",
                     from_='+12562426885',
                     to='+8615892562105'
                 )

print(message.sid)