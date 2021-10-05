import socket

HOST = "127.0.0.1"  # listen from localhost only
PORT = 65535  # non-reserved port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # TCP bind
    s.bind((HOST, PORT))

    # start listening for connections
    host_ip, host_port = s.getsockname()
    s.listen()
    print(f"[SocketEcho] Listening for connections on {host_ip}:{host_port}")

    # The server must keep running at this point, receiving requests and responding to them. So use a loop:
    while True:
        # call accept() method to receive any data that comes in
        # Python program will keep waiting until data is received
        # when data is received, accept() returns a tuple with 2 elements:
        # - conn_to_client: the connection object, used to communicate with client
        # - addr: a 2-ple containing the host & port (for IPv4)
        conn_to_client, addr = s.accept()
        host, port = addr  # The format of addr depends on the address family

        # receive data from client
        # Note that there is no way to know when the message has ended!
        # We will just assume it is <=1024 bytes :P
        msg = conn_to_client.recv(1024)

        # msg is in binary format, not text
        # call the bytes.decode() method to convert to text (UTF-8 by default)
        msg = msg.decode(encoding='utf-8')
        print(f"Message from {host}:{port}")
        print(msg)

        # Let's echo the client's message back to them
        # Data must be sent as bytes, not string. Use the str.encode() method to convert str to bytes
        conn_to_client.send(msg.encode())

        # We are done handling the request. We can close the connection here.
        conn_to_client.close()
