import socketserver

# source: [https://docs.python.org/3/library/socketserver.html#examples]


class MyTCPHandler(socketserver.StreamRequestHandler):

    def handle(self):
        # self.rfile is a file-like object created by the handler;
        # we can now use e.g. readline() instead of raw recv() calls
        data = self.rfile.readline().strip()

        print(f"{self.client_address[0]} wrote:\n"
              f"{data}")

        # Likewise, self.wfile is a file-like object used to write back
        # to the client
        self.wfile.write(replace(data))


def replace(b: bytes) -> bytes:
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö']
    text = b.decode()
    for c in text:
        if c in vowels:
            text = text.replace(c, '_')
    return text.encode()


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
