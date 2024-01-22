import socket
import threading


def handle_client(conn, addr):
    # 클라이언트 처리 함수
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # 클라이언트로부터 메시지 수신
        msg = conn.recv(1024).decode("utf-8")
        if msg:
            # 수신된 메시지 출력
            print(f"[{addr}] {msg}")

    # 연결 종료
    conn.close()


def start_server():
    # 서버 소켓 설정
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 50000))
    server.listen()

    print("[STARTING] Server is starting...")

    while True:
        # 클라이언트 연결 대기
        conn, addr = server.accept()
        # 새 클라이언트 연결에 대한 스레드 시작
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # 활성 연결 수 출력
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


if __name__ == "__main__":
    start_server()
