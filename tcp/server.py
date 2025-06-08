import socket

def start_server():
    # Input port dari user
    port = int(input("Masukkan port untuk server: "))
    
    # Buat socket TCP
    server_saya = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_saya.bind(('0.0.0.0', port))
    server_saya.listen(1)
    
    print(f"Server berjalan di port {port}, menunggu koneksi...")
    
    # Terima koneksi dari client
    client_socket, client_address = server_saya.accept()
    print(f"Terhubung dengan client: {client_address}")
    
    try:
        while True:
            # Terima pesan dari client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Client: {data}")
            
            # Kirim balasan ke client
            message = input("Anda (Server): ")
            client_socket.send(message.encode('utf-8'))
            
    except KeyboardInterrupt:
        print("\nServer dihentikan.")
    finally:
        client_socket.close()
        server_saya.close()

if __name__ == "__main__":
    start_server()
