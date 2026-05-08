#ex10_picosim_client_1vs1.py

import socket, time, random

def main():
    host = "127.0.0.1"
    port = 8000
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host,port))
        print("connected to server")
        for i in range(10):
            current_temp = round(random.uniform(20.0, 40.0), 1)
            client_socket.send(str(current_temp).encode('utf-8'))
            print(f"현재 온도 전송 : {current_temp}")
            response = client_socket.recv(1024).decode('utf-8')
            if response == "motor on":
                print("[pico motor on]")  
            elif response == "motor off":
                print("[pico motor off]")  
            print("-------")  
            time.sleep(2)
        
    except Exception as e:
        print(f"error : {e}")
    finally:
        client_socket.close()
        print("disconnected")
        
if __name__ == "__main__" :
    main()