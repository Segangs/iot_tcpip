# ex10_picosim_server_1vs1.py

import socket
def main():
    host = '127.0.0.1'
    port = 8000
    threshold = 30.0 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server started")
    conn, addr = server_socket.accept()
    print(f"client: {addr}")
    try:
        while True:
            data = conn.recv(1024). decode('utf-8')
            if not data : 
                break
            temp = float(data)
            print(f"수신 온도 : {temp}")
            if temp>threshold:
                response = "motor on"
            else:
                response = "motor off"
            conn.send(response.encode('utf-8'))
            print(f"제어 명령 전송 {response}")
    except Exception as e:
        print(f"error {e}")
    finally:
        conn.close()
        server_socket.close()
        print("server end")
        
if __name__  == "__main__" :
    main()