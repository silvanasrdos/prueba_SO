import socket
import random

SERV_PORT = 8081
BUF_SIZE = 100

def introducir_error(mensaje):
    if random.random() < 0.3:  # 30% de probabilidad
        mensaje_lista = list(mensaje)
        for _ in range(random.randint(1, 3)):  # Introducir 1 a 3 errores
            index = random.randint(0, len(mensaje_lista) - 1)
            mensaje_lista[index] = 'X'  # Introducir un error
        mensaje = ''.join(mensaje_lista)
    return mensaje

def main():
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockfd.bind(('127.0.0.1', SERV_PORT))
        sockfd.listen(5)
        print("[CANAL]: Esperando conexiones...")

        while True:
            connfd, client_addr = sockfd.accept()
            print(f"[CANAL]: Conexión aceptada de {client_addr}")

            while True:
                buff_rx = connfd.recv(BUF_SIZE).decode()
                if not buff_rx:
                    print("[CANAL]: Conexión cerrada por el cliente")
                    connfd.close()
                    break
                else:
                    mensaje_con_error = introducir_error(buff_rx)
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as dest_sock:
                        dest_sock.connect(('10.0.11.241', 8082))  # Cambia la IP al de tu máquina Windows
                        dest_sock.sendall(mensaje_con_error.encode())
                    print(f"[CANAL]: Enviado: {mensaje_con_error}")

    except Exception as e:
        print(f"[CANAL-error]: {e}")

if __name__ == "__main__":
    main()
