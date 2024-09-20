import socket
#import random
import hashlib

SERV_PORT = 8081
BUF_SIZE = 100

def calcular_control(cadena):
    return hashlib.md5(cadena.encode()).hexdigest()

def main():
    try:
        sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #esto es para el canal, para la fuenta sólo va connect():
        #sockfd.bind(('localhost', SERV_PORT)) #probado también con conexión local
        #sockfd.listen(5)
        sockfd.connect(('localhost', SERV_PORT))
        print("[FUENTE]: Esperando conexiones...")

        while True:
           
            print(f"[FUENTE]: Conexión aceptada de canal ")

            while True:

                # acá pareciera como que la fuente esta actuando de canal (debe encargarse sólo de enviar el mensaje)
                #buff_rx = connfd.recv(BUF_SIZE).decode()
                #if not buff_rx:
                 #   print("[FUENTE]: Conexión cerrada por el cliente")
                  #  connfd.close()
                   # break
                #else:

                mensaje = input("Ingrese el mensaje a enviar: ") + "\n"
                #control = calcular_control(buff_rx) esto lo sacaria
                #mensaje_con_control = f"{buff_rx}|{control}" esto tambien
                mensaje_con_control = calcular_control(mensaje)
                sockfd.sendall(mensaje_con_control.encode())  # Enviar mensaje al canal
                print(f"Mensaje enviado: {mensaje_con_control}")

    except Exception as e:
        print(f"[FUENTE-error]: {e}")

if __name__ == "_main_":
    main()