# ex12_flask_socket_server.py
# 온도 데이터를 받는 서버를 만든다.

# web server: 홈페이지같이 사람 대응(정적 서비스)
# WAS (Web App Server) : app대응 (동적 서비스) - 플라스크 해당

# flask : http 통신, was
# custom_thread : tcpip socket

# http상태코드

# 서버에는 스레드가 필요(플라스크와 소켓이 따로 돌아야 하기 때문)

import socket, threading
from flask import Flask, render_template_string

app = Flask(__name__)
# 센서데이터를 저장할 전역 변수
latest_sensor_data = ""

#---- TCP 소켓 ----
def start_tcp_server(host, port):
    global latest_sensor_data # 전역 변수로 설정
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"TCP 소켓 서버 : {host}:{port}에서 대기중..")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"연결됨 {address}")
        try:
            while True:
                data = client_socket.recv(1024)
                if not data: break
                latest_sensor_data = data.decode('utf-8')
                print(f"수신 {latest_sensor_data}")
        except Exception as e:
            print(f"Error {e}")
        finally:
            client_socket.close()
#---- Flask routing ---
@app.route("/")
def home():
    html = f"""
    <html>
    <head></head>
    <body>
    <h1>실시간 센서 값</h1>
    <p>현재 값:{latest_sensor_data}</p>
    <p>2초마다 자동 새로고침 중..</p>
    <script>setTimeout(function(){{location.reload();}}, 2000)</script>
    </body>
    
    </html>
    """
    return render_template_string(html)

if __name__ =="__main__" : 
    CLIENT_IP = "127.0.0.1"
    TCP_PORT = 9999
    tcp_thread = threading.Thread(target=start_tcp_server, args=(CLIENT_IP, TCP_PORT))
    tcp_thread.daemon = True # main 프로그램인 flask가 죽을때 같이 나도 같이 죽여주세용
    tcp_thread.start()
    app.run(host="127.0.0.1", port=5000)