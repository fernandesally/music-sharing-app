import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():

   
    print("\n\t\t\t\tMUSIC SHARING")

    #Client GUI starts here
    window=Tk()

    window.title('Share and Sing')
    window.geometry("300x300")
    window.configure(bg='LightSkyBlue')

    selectlabel = Label(window, text= "select your song",bg='LightSkyBlue', font = ("Calibri",10))
    selectlabel.place(x=1, y=2)

    listbox = Listbox(window,height = 10,width = 39,activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    playButton=Button(window,text="PLAY", width=10, bd=1,bg='LightSkyBlue', font = ("Calibri",10))
    playButton.place(x=30,y=200)

    stopButton=Button(window,text="STOP", width=10, bd=1, bg='LightSkyBlue', font = ("Calibri",10))
    stopButton.place(x=200,y=200)

    upload=Button(window,text="Upload",width=10, bd=1, bg='LightSkyBlue', font = ("Calibri",10))
    upload.place(x=30,y=250)

    download=Button(window,text="Download",width=10, bd=1, bg='LightSkyBlue', font = ("Calibri",10))
    download.place(x=200,y=250)

    infolabel=Label(window,text='', fg='blue', font = ("Calibri",10))
    infolabel.place(x=4,y=280)
    
    window.mainloop()



def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

   
    musicWindow()

setup()