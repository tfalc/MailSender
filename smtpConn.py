import smtplib, ssl

smtp_server = "" #include the smtp server from your e-mail. Example: smtp.gmail.com
port = 1 #change the number 1 to the port used by your stmp server. Usually 587, 25 or 465
sender_mail = "" #include your e-mail here
password = input("Enter your password to proceed: ")

# Creating a secure SSL context
context = ssl.create_default_context

try:
    server = smtplib.SMTP(smtp_server, port)
    server.starttls(context=context) # Securing the connection
    server.login(sender_mail, password)
    #TODO: Send email here
except Exception as e:
    # Error message
    print(e)
finally:
    server.quit()