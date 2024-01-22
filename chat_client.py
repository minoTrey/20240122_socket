import socket

def start_client():
    # 클라이언트 소켓 설정
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 50000))

    while True:
        # 사용자로부터 메시지 입력 받음
        msg = input("Message: ")
        # 입력 받은 메시지를 서버에 전송
        client.send(msg.encode("utf-8"))

if __name__ == "__main__":
    start_client()
