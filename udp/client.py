import socket

def run_udp_client():
    # Input alamat server dan port
    server_host = input("Masukkan alamat server: ")
    server_port = int(input("Masukkan port server: "))
    
    # Input port client
    client_port = int(input("Masukkan port untuk client: "))
    
    # Buat socket UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Bind ke port client (opsional untuk UDP, tapi berguna untuk menerima balasan)
    client_socket.bind(('0.0.0.0', client_port))
    
    server_address = (server_host, server_port)
    
    try:
        while True:
            # Kirim pesan ke server
            message = input("Pesan untuk server (ketik 'exit' untuk keluar): ")
            if message.lower() == 'exit':
                break
                
            client_socket.sendto(message.encode('utf-8'), server_address)
            
            # Terima balasan dari server
            data, _ = client_socket.recvfrom(1024)
            print(f"Balasan dari server: {data.decode('utf-8')}")
            
    except KeyboardInterrupt:
        print("\nClient dihentikan.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    run_udp_client()
