import scapy.all as scapy
import socket
import platform
import subprocess
import re

def get_network_prefix():
    """Mendeteksi IP Gateway dan Prefix Jaringan secara otomatis"""
    try:
        # Mendapatkan IP lokal perangkat ini
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        
        # Mengubah 192.168.1.5 menjadi 192.168.1.0/24
        prefix = re.sub(r'(\d+\.\d+\.\d+)\.\d+', r'\1.0/24', ip)
        return prefix
    except Exception:
        return "192.168.1.0/24" # Default jika gagal deteksi

def scan(ip):
    """Melakukan scanning menggunakan protokol ARP"""
    print(f"\n[+] Memulai Pemindaian Radar pada: {ip}")
    print("[+] Mengirim Paket ARP Request...\n")
    
    # Membuat paket ARP Request ke seluruh IP di jaringan
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    
    # Mengirim paket dan menerima respon
    answered_list = scapy.srp(arp_request_broadcast, timeout=2, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def display_result(results_list):
    print("------------------------------------------------------------")
    print("IP ADDRESS\t\tMAC ADDRESS\t\tVENDOR/INFO")
    print("------------------------------------------------------------")
    for client in results_list:
        # Coba ambil hostname (nama perangkat) jika tersedia
        try:
            hostname = socket.gethostbyaddr(client["ip"])[0]
        except socket.herror:
            hostname = "Unknown Device"
            
        print(f"{client['ip']}\t\t{client['mac']}\t{hostname}")

if __name__ == "__main__":
    print("""
    #########################################
    #       SPY-E NETWORK GUARDIAN          #
    #       Unit Intel: 123TOOL             #
    #########################################
    """)
    
    target_ip = get_network_prefix()
    scan_result = scan(target_ip)
    display_result(scan_result)
    
    print("\n[+] Pemindaian Selesai. Total Perangkat: " + str(len(scan_result)))
