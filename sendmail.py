import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "crackturtle126@gmail.com"  # Enter your address
receiver_email = "crackturtle126@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
message = """\
Subject: Hi there

This message is sent from Python."""

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("crackturtle126@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
