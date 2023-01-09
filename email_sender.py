import smtplib, ssl

smpt_server = "smtp.gmail.com"
port = 587
sender_email = "edwardsnowden2003@gmail.com"
receiver_email = "owaisalikhan2003@gmail.com"
password = "asd1fgh2jkl3"
message = "Testing. 1,2,3"

# For secure SSL context
context = ssl.create_default_context()

#Logging into google account and sending email
try:
    server = smtplib.SMTP(smpt_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print(e)
finally:
    server.quit()
