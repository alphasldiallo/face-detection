import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.
    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).decode("utf-8").strip()
        print(self.data)


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 1223

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        try:
            print("Starting the server on {}...".format(HOST))
            server.serve_forever()
        except KeyboardInterrupt:
            server.shutdown()
