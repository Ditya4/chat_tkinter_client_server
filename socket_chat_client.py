import socket
import tkinter as tk
from sys import exit



#===============================================================================
# def send_message(event):
#     print('Click')
#     text = edit_1.get()
#     print(text)
#     edit_1.delete(0, tk.END)
#===============================================================================
def send_to_server(user, text):
    global conn
    message = user + "~~~" + text
    conn.send(message.encode('utf-8'))
    print('send', message)


def pressed(event):
    #if event.char == 'a':
    print('Enter')
    text = edit_1.get()
    print(text)
    edit_1.delete(0, tk.END)
    send_to_server(USER, text)
    
def on_closing():
    global conn
    conn.close()
    exit()
    
    
def memo_1_add(text):
    print("memo_1 get text:", text)
    if '~~~~' in text:
        text = text.replace('~~~~', '')
    print('memo_1 text after replace:', text)
    if text.count('~~~') > 1:
        print('memo_1 ~~~ count > 1')
        
    user_end = text.find('~~~')
    user = text[:user_end]
    message_start = user_end + 3
    message = text[message_start:]
    memo_1.insert(tk.END, user + ': ' + message + '\n')
    
    


def update_clock():
    global conn
    conn.send('~~~~'.encode('utf-8'))
    received_bytes = conn.recv(1000)
    print("this_line", received_bytes)
    if received_bytes:
        received_text = received_bytes.decode('utf-8')
        if received_text != "~~~~":
            print('received text:', received_text)
            memo_1_add(received_text)
        else:
            print('(   ~~~~    )')
    root.after(2000, update_clock)
    

root = tk.Tk()

USER = "Ditya"
FORM_WEIGHT = 900
FORM_HEIGHT = 600
FORM_OFFSET_X = 200
FORM_OFFSET_Y = 100
root.geometry(str(FORM_WEIGHT) + 'x' + str(FORM_HEIGHT) +
               '+' + str(FORM_OFFSET_X) + '+' + str(FORM_OFFSET_Y))


string_variable = tk.StringVar()
string_variable.set('')
edit_1 = tk.Entry(root, textvariable=string_variable)
edit_1.focus_set()
edit_1.place(x=20, y=20)

send_button = tk.Button(root, text='Send')
send_button.place(x=20, y=60)
memo_1 = tk.Text(root)
memo_1.place(x=20, y=100)

conn = socket.socket()
conn.connect( ('127.0.0.1', 12351))

edit_1.bind("<Return>", pressed)
send_button.bind('<Button-1>', pressed)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.after(5000, update_clock)
tk.mainloop()

#from time import sleep
#===============================================================================
# conn = socket.socket()
# conn.connect( ('127.0.0.1', 12345))
# print('Enter next line("Exit" for quit):')
# while True:
#     text = input()
#     if text == 'Exit':
#         conn.close()
#         break
#     conn.send(text.encode('utf-8'))
#     data = conn.recv(1000)
#     print('Echo from server received, with text:', data.decode('utf-8'))
#     print('Enter next line("Exit" for quit):')
#===============================================================================
