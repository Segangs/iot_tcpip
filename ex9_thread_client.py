# ex9_thread_client.py

import socket, threading, sys


def send_msg(sock) :
    while True:
        message=input("your message : q to end")
        if message.lower() == 'q' :
            sock.close()
            break
        sock.send(message.encode('utf-8'))
        
def recv_msg(sock) :
    while True:
        try:
            data=sock.recv(1024)
            if not data: break
            print(f"received {data.decode('utf-8')}")
        except:
            break



def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <IP> <port>")
        sys.exit(1)
    
    #1. socket()
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM,
                         0)
    
    #2. 주소 설정
    serv_ip = sys.argv[1]
    serv_port = int (sys.argv[2])
    
    #3. connect()
    try:
        sock.connect((serv_ip, serv_port))
    except:
       print("connect error")
       return
        
    snd = threading.Thread(target=send_msg, args=(sock,))
    rcv = threading.Thread(target=recv_msg, args=(sock,))
    
    snd.start()
    rcv.start()
    
    snd.join()
    print("client terminated")
    

if __name__ == "__main__":
    main()
