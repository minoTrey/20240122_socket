import socket

def run_udp_client(server_host='127.0.0.1', server_port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = "Hello, UDP server"
        s.sendto(message.encode(), (server_host, server_port))
        # 서버로부터의 응답을 기다리지 않고 종료

if __name__ == "__main__":
    run_udp_client()
