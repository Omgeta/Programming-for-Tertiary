import socket

ADDR = ('127.0.0.1', 65535)

exit = False
while not exit:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(ADDR)
        msg = input("Say something ('exit' to quit): ")
        s.send(msg.encode())
        if msg == 'exit':
            exit = True
        else:
            resp = s.recv(1024)
            print("Response:", resp.decode())
