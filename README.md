## 📡 Wifi Network Guardian

Tool pemindai jaringan lokal untuk mendeteksi penyusup atau memantau perangkat yang terhubung.

## 📋 Prasyarat
- Python 3.x
- **Windows:** Instal [Npcap](https://nmap.org/npcap/) (Centang 'Install Npcap in WinPcap API-compatible Mode').
- **Linux:** `sudo apt install python3-scapy`

## ⚙️ Instalasi
1. Masuk ke folder proyek.
2. Instal library:
   ```bash
   pip install scapy

## ⚙️ Menjalankan
​PENTING : Harus dijalankan dengan hak akses Administrator/Root karena mengakses protokol jaringan tingkat rendah.

Windows : 
Buka CMD (Run as Administrator)
```
python network_scanner.py
```
Linux :
```
sudo python3 network_scanner.py
```

## Analisis Kerja :

1. ​**Protokol ARP :**
   Alat ini tidak pakai "Ping" biasa karena
   banyak perangkat (seperti iPhone atau
   Laptop modern) yang mematikan fitur Ping
   (ICMP) demi keamanan. Script kita pakai ARP
   (Address Resolution Protocol) yang sifatnya
   wajib di jaringan lokal, jadi perangkat
   "gaib" pun bakal ketahuan.
2. **​Auto-Detection :**
   Kamu gak perlu input IP manual. Script akan
   cek IP kamu sendiri lalu menebak range
   jaringannya (misal 192.168.1.0/24).
3. **​Hostname Discovery :**
   Alat mencoba menanyakan nama perangkat
   (hostname) ke sistem DNS lokal agar kamu
   tahu mana yang HP Android, Laptop, atau
   CCTV.
