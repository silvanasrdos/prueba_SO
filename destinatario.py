import socket
import hashlib

SERVER_ADDRESS = "10.0.11.241"  # Cambia esto a la IP de tu máquina Windows
PORT = 8082
BUF_SIZE = 100

def verificar_control(mensaje):
    try:
        mensaje_original, control_recibido = mensaje.rsplit('|', 1)
        control_calculado = hashlib.md5(mensaje_original.encode()).hexdigest()
        return mensaje_original, control_recibido == control_calculado
    except ValueError:
        return None, False

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.bind((SERVER_ADDRESS, PORT))
        sock.listen(5)
        print("DESTINATARIO: Esperando conexiones...")

        connfd, addr = sock.accept()
        print(f"DESTINATARIO: Conectado desde {addr}")

        while True:
            buf_rx = connfd.recv(BUF_SIZE).decode()
            if not buf_rx:
                print("DESTINATARIO: Conexión cerrada por el canal.")
                break

            mensaje, es_correcto = verificar_control(buf_rx)

            if es_correcto:
                print("DESTINATARIO: Mensaje correcto:", mensaje)
            else:
                print("DESTINATARIO: Mensaje con errores:", buf_rx)

    except socket.error as e:
        print("Error en el socket:", e)

    finally:
        sock.close()

if __name__ == "__main__":
    main()
