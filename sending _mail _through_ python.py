import emails

def mail(gmail,name,reciept_no):
    
    subject="Hi "+name+" your receipt no. is"+reciept_no

    message = emails.html(html="<p>Hi!<br>Here is your receipt...",
                              subject=subject,
                              mail_from=('DEEPIKA', 'pqr@gmail.com'))

    r = message.send(to='xyz@gmail.com', smtp={'host': 'smtp.gmail.com', 'timeout': 5,
                                                      'port':587,
                                                      'user':'abc@gmail.com',
                                                      'password':'1234',
                                                      'tls':True})

    print(r.status_code)
g=input("Enter gmail")
n=input("Enter name")
rn=input("Enter reciept no")
mail(g,n,rn)
