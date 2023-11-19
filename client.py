import socket
from tkinter import Tk  # Python 3
#from Tkinter import Tk # for Python 2.x
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))

done = False

try:
    Copy = Tk().clipboard_get()
except:
    pass

while not done:
    try:
        Check = Tk().clipboard_get()
        if Check != Copy:
            print('Copy detected')
            Copy = Check
            client.send(Copy.encode('utf-8'))

    except:
        pass








