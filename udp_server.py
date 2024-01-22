import socket

def run_udp_server(port=65432):
    # 소켓 객체 생성 (AF_INET: IPv4, SOCK_DGRAM: UDP)
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # 주소와 포트 바인딩
        s.bind(('127.0.0.1', port))
        while True:
            # 클라이언트로부터 데이터 수신
            data, addr = s.recvfrom(1024)
            # 수신한 데이터와 클라이언트 주소 출력
            print(f"Received (UDP): {data.decode()} from {addr}")

if __name__ == "__main__":
    run_udp_server()
