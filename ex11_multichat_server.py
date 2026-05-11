# ex11_multichat_server.py    여러 명의 채팅
# 서버는 클라이언트 접속을 관리, 브로드 캐스트(접속한 모두에게 전파)

import socket, threading

HOST = "127.0.0.1"
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()


clients = []
nicknames = []


# 모든 클라이언트에게 대화메세지 전송
def broadcast(message):
    for client in clients:
        client.send(message)


# 클라이언트 메세지 처리
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()  #클라이언트 몇번째 사람이 나갔는지 확인하고 소켓 닫고, 목록에서 삭제
            nickname = nicknames[index]
            broadcast(f"{nickname}님이 나갔습니다.".encode('utf-8'))
            nicknames.remove(nickname)
            break


def main():
    print("서버 시작. 연결을 기다립니다.")
    while True:
        client, address = server.accept()
        print(f"연결 성공 : {str(address)}")
        client.send("NICK".encode("utf-8"))
        nickmane = client.recv(1024).decode("utf-8")
        nicknames.append(nickmane)
        clients.append(client)

        print(f"사용자 닉네임: {nickmane}")

        broadcast(f"{nickmane}님이 입장하였습니다.".encode('utf=8'))
        client.send("서버에 연결되었어용".encode('utf=8'))

        thread = threading.Thread(target=handle, args = (client, ))
        thread.start()


if __name__ == "__main__":
    main()
