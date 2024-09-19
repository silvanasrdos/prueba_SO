import socket
#import random
import hashlib

SERV_PORT = 8080
BUF_SIZE = 100

def calcular_control(cadena):
    return hashlib.md5(cadena.encode()).hexdigest()

def main():
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockfd.bind(('192.168.1.21', SERV_PORT)) #probado también con conexión local
        sockfd.listen(5)
        print("[FUENTE]: Esperando conexiones...")

        while True:
            connfd, client_addr = sockfd.accept()
            print(f"[FUENTE]: Conexión aceptada de {client_addr}")

            while True:
                buff_rx = connfd.recv(BUF_SIZE).decode()
                if not buff_rx:
                    print("[FUENTE]: Conexión cerrada por el cliente")
                    connfd.close()
                    break
                else:
                    control = calcular_control(buff_rx)
                    mensaje_con_control = f"{buff_rx}|{control}"
                    connfd.sendall(mensaje_con_control.encode())
                    print(f"[FUENTE]: Enviado: {mensaje_con_control}")

    except Exception as e:
        print(f"[FUENTE-error]: {e}")

if __name__ == "__main__":
    main()
