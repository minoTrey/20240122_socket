import socket

def run_tcp_server(port=65432):
    # 소켓 객체 생성 (AF_INET: IPv4, SOCK_STREAM: TCP)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # 주소와 포트 바인딩
        s.bind(('127.0.0.1', port))
        # 클라이언트의 연결 요청 대기
        s.listen()
        # 연결 요청 수락
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                # 클라이언트로부터 데이터 수신
                data = conn.recv(1024)
                if not data:
                    break
                # 수신한 데이터 출력
                print(f"Received (TCP): {data.decode()}")
                # 수신한 데이터를 그대로 클라이언트에게 전송
                conn.sendall(data)

if __name__ == "__main__":
    run_tcp_server()
