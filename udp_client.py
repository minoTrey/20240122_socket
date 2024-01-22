import socket

def run_udp_client(server_host='127.0.0.1', server_port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # 서버에 메시지 전송
        message = "Hello, UDP server"
        s.sendto(message.encode(), (server_host, server_port))
        # 서버로부터 데이터 수신
        data, addr = s.recvfrom(1024)
        # 수신한 데이터 출력
        print('Received:', data.decode())

if __name__ == "__main__":
    run_udp_client()
