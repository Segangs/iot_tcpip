import socket, sys

def main():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    server_addr = ("163.152.213.114", 8001)
    
    sock.sendto(b'Hello~~~', server_addr)
    
    try:
        data, addr = sock.recvfrom(1024)
        print(f"Message from server: {data.decode('utf-8')}")
        
    except Exception as e:
        print(f"Error: {e}")
        sock.close()
if __name__ == "__main__": 
    main() 