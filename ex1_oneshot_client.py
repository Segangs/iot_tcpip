# ex1_oneshot_client.py 교재 P25 (hello.c 를 python으로 다시 작성)

#서버 실행 :  python ~server.py 8000
#클라이언트 실행 : python ~client.py 127.0.0.1 8000

import socket
import sys


def error_handling(message):
    sys.stderr.write(message + "\n")
    sys.exit(1)


def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <IP> <port>")
        sys.exit(1)
    
    #1. socket()
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM,
                         0)
    
    if sock.fileno() == -1:
        error_handling("socket() error")
    
    #2. 주소 설정
    serv_ip = sys.argv[1]
    serv_port = int (sys.argv[2])
    
    #3. connect()
    try:
        sock.connect((serv_ip, serv_port))
    except:
        error_handling("socket connect() error")
        
    #4. read() 응답 받기
    try:
        message_from_server = sock.recv(30)  # 30은 버퍼 사이즈
        if not message_from_server:
            error_handling("no contents error")
        print(f"Message from server: { message_from_server.decode('utf-8') }")
    except socket.error:
        error_handling("read() error")
    sock.close()
        

if __name__ == "__main__":
    main()
