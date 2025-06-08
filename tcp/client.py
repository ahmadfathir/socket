import socket

def start_client():
    # Input host dan port dari user
    host = input("Masukkan alamat server (localhost jika di komputer yang sama): ")
    port = int(input("Masukkan port server: "))
    
    # Buat socket TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((host, port))
        print(f"Terhubung ke server {host}:{port}")
        
        while True:
            # Kirim pesan ke server
            message = input("Anda (Client): ")
            client_socket.send(message.encode('utf-8'))
            
            # Terima balasan dari server
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Server: {data}")
            
    except ConnectionRefusedError:
        print("Tidak dapat terhubung ke server. Pastikan server sedang berjalan.")
    except KeyboardInterrupt:
        print("\nClient dihentikan.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()
