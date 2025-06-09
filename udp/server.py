import socket

def run_udp_server():
    # Input port dari user
    server_port = int(input("Masukkan port untuk server: "))
    
    # Buat socket UDP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind ke port
    server_socket.bind(('0.0.0.0', server_port))
    print(f"Server UDP berjalan di port {server_port}")
    
    # Dictionary untuk menyimpan alamat client
    clients = {}
    
    try:
        while True:
            # Terima data dari client
            data, client_address = server_socket.recvfrom(1024)
            
            # Simpan alamat client jika baru
            if client_address not in clients:
                clients[client_address] = True
                print(f"Client terhubung: {client_address}")
            
            # Decode pesan
            message = data.decode('utf-8')
            print(f"Pesan dari {client_address}: {message}")
            
            # Kirim balasan
            reply = input("Balasan untuk client: ")
            server_socket.sendto(reply.encode('utf-8'), client_address)
            
    except KeyboardInterrupt:
        print("\nServer dihentikan.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_udp_server()
