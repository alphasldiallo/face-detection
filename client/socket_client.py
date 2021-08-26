    import socket
    import sys, time


    def main():
        target_host = '172.20.10.2'
        target_port = 1223

        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print('Could not create a socket')
            time.sleep(1)
            sys.exit()

        try:
            client.connect((target_host, target_port))
        except socket.error:
            print('Could not connect to server')
            time.sleep(1)
            sys.exit()

        online = True
        while online:
            for i in range(10):
                client.sendall(str(i).encode())
                time.sleep(1)


    # start client
    main()