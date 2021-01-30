from app.api.interface import Connection
from app.api.contact_api import Methods
import multiprocessing
import time
import asyncio


class Request:
    def __init__(self, interface: Connection):
        self.interface = interface

    def add(self, target: str, conn):
        if self.interface.put(target):
            conn.write(b'\n')
            conn.write(bytes("HTTP/1.1  201 created".encode("UTF-8")))
        else:
            conn.write(b'\n')
            conn.write(bytes("HTTP/1.1 403 Forbidden".encode("UTF-8")))

    def load(self, target: str, conn):
        conn.write(b'\n')
        if self.interface.get(target)[0].id == "":
            conn.write(bytes("HTTP/1.1 404 Not Found".encode("UTF-8")))
        else:
            for i in range(len(self.interface.get(target))):
                conn.write(bytes(self.interface.get(target)[i].name.ljust(20),
                                 encoding="UTF-8"))
                conn.write(bytes(self.interface.get(target)[i].address.ljust(20),
                                 encoding="UTF-8"))
                conn.write(bytes(self.interface.get(target)[i].phone.ljust(20),
                                 encoding="UTF-8"))
                conn.write(bytes(self.interface.get(target)[i].id.ljust(7),
                                 encoding="UTF-8"))
                conn.write(b'\n')
            conn.write(bytes("HTTP/1.1 200 OK".ljust(25), encoding="UTF-8"))

    def edit(self, target: str, conn):
        conn.write(b'\n')
        if self.interface.post(target):
            conn.write(bytes("HTTP/1.1 200 OK".ljust(25), encoding="UTF-8"))
        else:
            conn.write(bytes("HTTP/1.1 403 Forbidden".ljust(25),
                             encoding="UTF-8"))

    def delt(self, target: str, conn):
        conn.write(b'\n')
        if self.interface.delete(target):
            conn.write(bytes("HTTP/1.1 200 OK".ljust(25), encoding="UTF-8"))
        else:
            conn.write(bytes("HTTP/1.1 404 Not Found".ljust(25),
                             encoding="UTF-8"))


async def server(reader, writer):
    print('Connection from {}'.format(writer.get_extra_info('peername')))
    process = multiprocessing.Process()
    procs.append(process)
    process.start()
    while True:
        try:
            data = await reader.read(1024)
            arr = data.decode('UTF-8').split()
            z = Methods()
            if not data:
                print("Terminating connection")
                writer.close()
                break
            if arr[0] == 'PUT':
                start = time.time()
                Request(z).add(arr[1], writer)
                print(time.time() - start)
            if arr[0] == 'GET':
                start = time.time()
                Request(z).load(arr[1], writer)
                print(time.time() - start)
            if arr[0] == 'POST':
                start = time.time()
                Request(z).edit(arr[1], writer)
                print(time.time() - start)
            if arr[0] == 'DELETE':
                start = time.time()
                Request(z).delt(arr[1], writer)
                print(time.time() - start)
        except ConnectionResetError:
            break
        except:
            writer.write(bytes("\n HTTP/1.1 400 Bad Request".ljust(25),
                               encoding="UTF-8"))
        finally:
            process.join()
            writer.close()


procs = []


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    server_corotine = loop.run_until_complete(asyncio.ensure_future
                                              (asyncio.start_server
                                               (server, "127.0.0.1", 9090),
                                               loop=loop))
    loop.run_forever()
