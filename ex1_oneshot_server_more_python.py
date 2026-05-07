# ex1_oneshot_server_more_python.py 교재 P21 조금더 파이선스럽게 작성

# 서버 실행 :  python ~server.py 8000
# 클라이언트 실행 : python ~client.py 127.0.0.1 8000
import socket
import sys


def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <port>")
        sys.exit(1)

    serv_ip = "" # 127.0.0.1
    serv_port = int(sys.argv[1])  # ex 8000

    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)     # 1. socket (21)

    try:
        serv_sock.bind((serv_ip, serv_port))  # 3. 초기화
        serv_sock.listen(5) == -1  # 4. listen()
        print("NOW I am listening!")

        clnt_sock, clnt_addr = serv_sock.accept()  # 5. accept()
        print(f"connected from {clnt_addr}")

        message = "hello this is server speaking"  # 6. write()
        clnt_sock.send(message.encode("utf-8"))
        clnt_sock.close()

    except Exception as e:
        print(f"error :{e}")

    finally:
        serv_sock.close()  # 서버 닫기

    # C언어 : ifndef


if __name__ == "__main__":
    main()
