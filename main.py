import socket
from datetime import datetime

# Kullanıcıdan hedef IP ve port aralığını alıyoruz
target_ip = input("Hedef IP adresini girin: ")
start_port = int(input("Başlangıç portunu girin: "))
end_port = int(input("Bitiş portunu girin: "))

# Tarama başlangıcını kaydediyoruz
print("\nPort taraması başlıyor...")
start_time = datetime.now()

# Hedef IP'ye bağlanarak portları kontrol ediyoruz
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.01)  # Bağlantı süresi
    result = sock.connect_ex((target_ip, port))  # Portu kontrol et

    if result == 0:
        print(f"Port {port} açık")
    else:
        print(f"Port {port} kapalı")
    
    sock.close()

# Tarama bitişi
end_time = datetime.now()
total_time = end_time - start_time
print(f"\nTarama tamamlandı. Toplam süre: {total_time}")
