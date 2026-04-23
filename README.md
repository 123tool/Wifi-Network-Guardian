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

Windows : Buka CMD (Run as Administrator)
```
python network_scanner.py
```
Linux :
```
sudo python3 network_scanner.py
