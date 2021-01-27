from app.interface import Connection
from API.contactAPI import Methods
import socket


class Request:
    def __init__(self, interface: Connection):
        self.interface = interface

    def add(self, target: str):
        return self.interface.put(target)

    def load(self, target: str):
        return self.interface.get(target)

    def edit(self, target: str):
        return self.interface.post(target)

    def delt(self, target: str):
        return self.interface.delete(target)


while True:
    sock = socket.socket()
    sock.bind(('127.0.0.1', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    arr = data.decode('UTF-8').split()
    z = Methods()
    try:
        if arr[0] == 'PUT' and Request(z).add(arr[1]):
            Request(z).add(arr[1])
            conn.send(bytes("HTTP/1.1  201 created".encode("UTF-8")))
        elif arr[0] == 'PUT' and not Request(z).add(arr[1]):
            conn.send(bytes("HTTP/1.1 403 Forbidden".encode("UTF-8")))

        if arr[0] == 'GET':
            array = Request(z).load(arr[1])
            if array[0].name == "" and array[0].address == "" and \
                    array[0].phone == "" and array[0].id == "":
                conn.send(b'\n')
                conn.send(bytes("HTTP/1.1 404 Not Found".encode("UTF-8")))
            else:
                for i in range(len(array)):
                    conn.send(b'\n')
                    conn.send(bytes(array[i].name.ljust(20), encoding="UTF-8"))
                    conn.send(bytes(array[i].address.ljust(20),
                                    encoding="UTF-8"))
                    conn.send(bytes(array[i].phone.ljust(20),
                                    encoding="UTF-8"))
                    conn.send(bytes(array[i].id.ljust(7),
                                    encoding="UTF-8"))
                    conn.send(b'\n')
                conn.send(bytes("HTTP/1.1 200 OK".ljust(25), encoding="UTF-8"))

        if arr[0] == 'POST' and Request(z).edit(arr[1]):
            Request(z).edit(arr[1])
            conn.send(b'\n')
            conn.send(bytes("HTTP/1.1 200 OK".ljust(25), encoding="UTF-8"))
        elif arr[0] == 'POST' and not Request(z).edit(arr[1]):
            conn.send(b'\n')
            conn.send(bytes("HTTP/1.1 403 Forbidden".ljust(25),
                            encoding="UTF-8"))

        if arr[0] == 'DELETE' and Request(z).delt(arr[1]):
            Request(z).delt(arr[1])
            conn.send(b'\n')
            conn.send(bytes("HTTP/1.1 200 OK".ljust(25), encoding="UTF-8"))
        elif arr[0] == 'DELETE' and not Request(z).delt(arr[1]):
            conn.send(b'\n')
            conn.send(bytes("HTTP/1.1 404 Not Found".ljust(25),
                            encoding="UTF-8"))
    except:
        conn.send(b'\n')
        conn.send(bytes("HTTP/1.1 400 Bad Request".ljust(25),
                        encoding="UTF-8"))
    finally:
        conn.close()

