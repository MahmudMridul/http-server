import socket

HOST = ""
PORT = 8080


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(1)
        conn, addr = server.accept()
        with conn:
            print("connected by ", addr)
            data = conn.recv(512)
            if data:
                conn.sendall(data)


if __name__ == "__main__":
    main()
