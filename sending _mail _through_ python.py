import emails



message = emails.html(html="<p>Hi!<br>Here is your receipt...",
                          subject="your receipt no. is 23456",
                          mail_from=('DEEPIKA', 'pqr@gmail.com'))

r = message.send(to='xyz@gmail.com', smtp={'host': 'smtp.gmail.com', 'timeout': 5,
                                                  'port':587,
                                                  'user':'abc@gmail.com',
                                                  'password':'1234',
                                                  'tls':True})

print(r.status_code)
