import socket
import random

CANAL_PORT = 8081
BUF_SIZE = 100
DESTINATARIO_IP = '127.0.0.1'  # IP a la de tu máquina Windows
DESTINATARIO_PORT = 8082  # Puerto del Destinatario en Windows

def introducir_error(mensaje):
    if random.random() < 0.3:  # 30% de probabilidad
        mensaje_lista = list(mensaje)
        for _ in range(random.randint(1, 3)):  # Introduce 1 a 3 errores
            index = random.randint(0, len(mensaje_lista) - 1)
            mensaje_lista[index] = 'X'  # Introducir un error
        mensaje = ''.join(mensaje_lista)
    return mensaje

def main():
        # Crear el socket para escuchar conexiones desde la fuente
        canal_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        canal_socket.bind(('127.0.0.1', CANAL_PORT))
        canal_socket.listen(5)
        print("[CANAL]: Esperando conexiones de la fuente...")

        while True:
            # Aceptar la conexión de la fuente
          
            connfd, fuente_addr = canal_socket.accept()
            #print(f"[CANAL]: Conexión aceptada de la fuente en {fuente_addr}")

            while True:
                # Recibir mensaje desde la fuente
                buff_rx = connfd.recv(BUF_SIZE).decode()
                if not buff_rx:
                    print("[CANAL]: Conexión cerrada por la fuente")
                    connfd.close()
                    break
                else:
                    # Introduce posibles errores en el mensaje
                    mensaje_con_error = introducir_error(buff_rx)

                    # Conecta con el Destinatario para reenviar el mensaje
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as dest_sock:
                        dest_sock.connect((DESTINATARIO_IP, DESTINATARIO_PORT))
                        dest_sock.sendall(mensaje_con_error.encode())
                    
                    print(f"[CANAL]: Mensaje enviado al Destinatario con posibles errores: {mensaje_con_error}")

if __name__ == "_main_":
    main()