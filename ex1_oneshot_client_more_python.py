# ex1_oneshot_client_more_python.py 교재 P25 (hello.c 를 python으로 다시 작성)

#서버 실행 :  python ~server.py 8000
#클라이언트 실행 : python ~client.py 127.0.0.1 8000

import socket
import sys

def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <IP> <port>")
        sys.exit(1)
        
    serv_ip = sys.argv[1]
    serv_port = int (sys.argv[2])
    
    #1. socket()
    
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM,
                         0)
    
    try:
        sock.connect((serv_ip, serv_port))     #3. connect()
        message_from_server = sock.recv(1024)  # 1024는 표준 버퍼 사이즈
        if not message_from_server:
            print("no contents error")
        print(f"Message from server: { message_from_server.decode('utf-8') }")
    except Exception as e:
        print(f"error: {e}")
    finally:
        sock.close()        

if __name__ == "__main__":
    main()
