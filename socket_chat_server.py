import socket
from random import choice, randint

sock = socket.socket()
list_of_messages = ['Zeus~~~Где мой топор?',
                    'Demon~~~А я осиновый кол точу',
                    'Кузенька~~~Ой беда, беда, огорчение.']
sock.bind( ("127.0.0.1", 12351) )
#      ('127.0.0.1', port)
sock.listen(10)
print(0)
conn1, addr1 = sock.accept()

while True:
    data = conn1.recv(1000)
    if data:
        text = data.decode('utf-8')
        if text == "~~~~":
            pass
            if randint(0, 6) == 1:
                data = choice(list_of_messages).encode('utf-8')
                # data = 'Zeus~~~Где мой топор?'.encode('utf-8')
    #       pass
    conn1.send(data)

conn1.close()