import socket

HOST = ""
PORT = 8080


def prepare_get_response() -> str:
    body = "nothing to get from this server."
    content_length = len(body.encode())
    response = (
        "HTTP/1.1 200 OK\r\n"
        + "Content-Type:text/plain\r\n"
        + f"Content-Length:{content_length}\r\n\r\n{body}"
    )
    return response


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(1)
        conn, addr = server.accept()
        with conn:
            print("connected by ", addr)
            data = conn.recv(512)
            if data:
                list = data.split(sep=b"\r\n")
                status = list[0].split(b" ")

                if status[0] == b"GET":
                    print("start processing GET request")
                    response = prepare_get_response()
                    conn.sendall(response.encode())


if __name__ == "__main__":
    main()
