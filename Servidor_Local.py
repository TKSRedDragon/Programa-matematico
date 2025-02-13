import socket
import threading

host = "0.0.0.0"  # Escucha en todas las interfaces
port = 12345

modo = input("Escribe 'servidor' o 'cliente': ").strip().lower()

if modo == "servidor":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    clientes = {}  # Diccionario de clientes {conn: nombre}

    def manejar_cliente(conn, addr):
        """ Maneja la comunicación con un cliente específico """
        conn.send("Introduce tu nombre de usuario: ".encode())
        nombre = conn.recv(1024).decode().strip()
        clientes[conn] = nombre

        print(f"[+] {nombre} ({addr}) se ha conectado.")
        for cliente in clientes:
            if cliente != conn:
                cliente.send(f"[Servidor] {nombre} se ha unido al chat.".encode())

        while True:
            try:
                mensaje = conn.recv(1024).decode()
                if not mensaje:
                    break

                print(f"[{nombre}] {mensaje}")

                # Reenviar mensaje a todos los clientes
                for cliente in clientes:
                    if cliente != conn:
                        cliente.send(f"[{nombre}] {mensaje}".encode())

            except:
                break

        print(f"[-] {nombre} ({addr}) se ha desconectado.")
        for cliente in clientes:
            if cliente != conn:
                cliente.send(f"[Servidor] {nombre} ha salido del chat.".encode())

        del clientes[conn]
        conn.close()

    def enviar_mensajes():
        """ Permite al servidor enviar mensajes a los clientes y verlo en consola """
        while True:
            mensaje = input("Servidor: ")
            if mensaje.lower() == "salir":
                break
            print(f"[Servidor] {mensaje}")
            for cliente in clientes:
                cliente.send(f"[Servidor] {mensaje}".encode())

    print(f"Servidor escuchando en {host}:{port}...")

    # Hilo para enviar mensajes desde el servidor
    threading.Thread(target=enviar_mensajes, daemon=True).start()

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=manejar_cliente, args=(conn, addr), daemon=True).start()

else:
    server_ip = input("Introduce la IP del servidor: ").strip()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    def recibir_mensajes():
        """ Recibe mensajes del servidor o de otros clientes """
        while True:
            try:
                mensaje = client_socket.recv(1024).decode()
                if not mensaje:
                    break
                print(mensaje)
            except:
                break

    # Iniciar hilo para recibir mensajes
    threading.Thread(target=recibir_mensajes, daemon=True).start()

    # Enviar nombre de usuario
    print(client_socket.recv(1024).decode(), end="")  # "Introduce tu nombre de usuario:"
    nombre_usuario = input().strip()
    client_socket.send(nombre_usuario.encode())

    while True:
        mensaje = input(f"{nombre_usuario}: ")
        if mensaje.lower() == "salir":
            break
        client_socket.send(mensaje.encode())

    client_socket.close()