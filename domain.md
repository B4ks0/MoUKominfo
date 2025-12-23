# Tutorial Sambung Domain ke Django di VM (via Nginx)

Panduan ini menjelaskan cara menghubungkan domain ke aplikasi Django yang berjalan di Virtual Machine (VM) menggunakan Nginx sebagai reverse proxy.

## Arsitektur

```
Internet
   ↓
Domain (example.com)
   ↓
IP Publik VM
   ↓
Nginx (port 80 / 443)
   ↓
Django (127.0.0.1:8000)
```

> **Catatan:** Django tidak boleh diekspos langsung ke internet. Nginx bertugas menangani request publik.

---

## LANGKAH 1 — Arahkan DOMAIN ke IP VM

Masuk ke **DNS Manager domain kamu** (Niagahoster, Rumahweb, Cloudflare, dll).

Buat **A Record**:

| Type | Name  | Value          |
| ---- | ----- | -------------- |
| A    | `@`   | `IP_PUBLIK_VM` |
| A    | `www` | `IP_PUBLIK_VM` |

Contoh:

```
example.com → 103.xxx.xxx.xxx
www.example.com → 103.xxx.xxx.xxx
```

⏳ Tunggu propagasi DNS (1 menit - 1 jam).

---

## LANGKAH 2 — Jalankan Django di VM

Di dalam VM, jalankan server development (untuk testing):

```bash
python manage.py runserver 127.0.0.1:8000
```

> **PENTING:** Jangan gunakan `0.0.0.0:8000` untuk production karena tidak aman.

---

## LANGKAH 3 — Install Nginx di VM

```bash
sudo apt update
sudo apt install nginx -y
```

Cek status:

```bash
systemctl status nginx
```

Buka browser dan akses `http://IP_VM`. Jika muncul **"Welcome to Nginx"**, berarti instalasi berhasil.

---

## LANGKAH 4 — Konfigurasi Nginx → Django

### Buat config baru:

```bash
sudo nano /etc/nginx/sites-available/django
```

Isi dengan konfigurasi berikut (ganti `example.com` dengan domain Anda):

```nginx
server {
    listen 80;
    server_name example.com www.example.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Aktifkan konfigurasi:

```bash
sudo ln -s /etc/nginx/sites-available/django /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

---

## LANGKAH 5 — Set `ALLOWED_HOSTS` Django

Edit file `settings.py`:

```python
ALLOWED_HOSTS = [
    "example.com",
    "www.example.com",
    "IP_VM"
]
```

Restart Django:

```bash
CTRL + C
python manage.py runserver 127.0.0.1:8000
```

---

## LANGKAH 6 — TEST

Buka browser dan akses:

```
http://example.com
```

🎉 **Domain sekarang mengarah ke Django (localhost:8000)**

---

## (OPSIONAL) HTTPS dengan SSL Gratis (Certbot)

Untuk production, wajib menggunakan HTTPS.

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d example.com -d www.example.com
```

Nginx akan otomatis dikonfigurasi untuk menggunakan HTTPS.

---

## RANGKUMAN

| Pertanyaan                              | Jawaban             |
| --------------------------------------- | ------------------- |
| Domain ke localhost:8000 bisa langsung? | ❌ Tidak             |
| Harus hosting?                          | ✅ VM kamu = hosting |
| Butuh Nginx?                            | ✅ WAJIB             |
| Django langsung expose ke publik?       | ❌ Jangan            |

---

# ADD ON: 1 VM, 5 Domain, 5 Django App?

Pertanyaan: *Kalau ada 5 domain dan di VM ada 5 website Django lagi sedang run di port berbeda beda? 8001, 8002, etc??*

Jawaban: **✅ BISA, dan itu sangat normal.**
Ini namanya **virtual hosting + reverse proxy**. Standar industri.

## GAMBAR BESARNYA

```
Domain A ──┐
Domain B ──┼──► IP VM ─► NGINX (80/443)
Domain C ──┘                 │
                              ├── Django A → 127.0.0.1:8001
                              ├── Django B → 127.0.0.1:8002
                              ├── Django C → 127.0.0.1:8003
                              ├── Django D → 127.0.0.1:8004
                              └── Django E → 127.0.0.1:8005
```

*   👉 **1 VM, 1 IP publik, banyak domain, banyak Django app**
*   👉 **Port 8001-8005 tidak terekspos ke internet, cuma lokal.**

---

## LANGKAH 1 — DNS SEMUA DOMAIN → 1 IP VM

Arahkan **semua domain** ke IP Publik VM yang sama.

| Domain | Record | Value |
| :--- | :--- | :--- |
| `domain1.com` | A | `IP_VM` |
| `domain2.com` | A | `IP_VM` |
| `domain3.com` | A | `IP_VM` |
| `domain4.com` | A | `IP_VM` |
| `domain5.com` | A | `IP_VM` |

---

## LANGKAH 2 — Pastikan SETIAP Django jalan di port beda

Jalankan masing-masing aplikasi di port terpisah:

```bash
# Website 1
python manage.py runserver 127.0.0.1:8001

# Website 2
python manage.py runserver 127.0.0.1:8002

# Website 3
python manage.py runserver 127.0.0.1:8003
```

> ⚠️ **Catatan:** Untuk production, gunakan **Gunicorn** atau **Uvicorn**, jangan `runserver`. `runserver` hanya untuk contoh biar paham konsep portnya.

---

## LANGKAH 3 — NGINX: 1 DOMAIN = 1 SERVER BLOCK

Buat konfigurasi berbeda untuk setiap domain di `/etc/nginx/sites-available/`.

**Contoh Config Website 1 (domain1):**
```nginx
server {
    listen 80;
    server_name domain1.com www.domain1.com;

    location / {
        proxy_pass http://127.0.0.1:8001; # Arahkan ke port 8001
        include proxy_params;
    }
}
```

**Contoh Config Website 2 (domain2):**
```nginx
server {
    listen 80;
    server_name domain2.com www.domain2.com;

    location / {
        proxy_pass http://127.0.0.1:8002; # Arahkan ke port 8002
        include proxy_params;
    }
}
```

➡️ **Ulangi sampai 5 domain.**

Aktifkan semuanya:
```bash
sudo ln -s /etc/nginx/sites-available/domain1 /etc/nginx/sites-enabled/
sudo ln -s /etc/nginx/sites-available/domain2 /etc/nginx/sites-enabled/
# ... dst
sudo nginx -t
sudo systemctl reload nginx
```

---

## LANGKAH 4 — ALLOWED_HOSTS TIAP DJANGO

Setiap aplikasi Django harus tahu nama domainnya sendiri.

**Di `settings.py` Website 1:**
```python
ALLOWED_HOSTS = ["domain1.com", "www.domain1.com"]
```

**Di `settings.py` Website 2:**
```python
ALLOWED_HOSTS = ["domain2.com", "www.domain2.com"]
```

➡️ **WAJIB spesifik per domain.**

---

## LANGKAH 5 — HTTPS (Satu Command Semua Domain)

Kamu bisa request SSL sekaligus atau satu-satu.

```bash
sudo certbot --nginx \
 -d domain1.com -d www.domain1.com \
 -d domain2.com -d www.domain2.com \
 -d domain3.com -d www.domain3.com \
 -d domain4.com -d www.domain4.com \
 -d domain5.com -d www.domain5.com
```

Certbot akan otomatis mendeteksi server block yang sesuai di Nginx dan menginstalkan sertifikat SSL.

---

## REALITA & BEST PRACTICE

| Hal | Status | Keterangan |
| :--- | :--- | :--- |
| **1 VM banyak Django** | ✅ Normal | Hemat biaya infrastruktur |
| **1 IP banyak domain** | ✅ Normal | IP publik itu mahal, ini solusinya |
| **Port Django beda-beda** | ✅ Normal | Biar gak bentrok (collision) |
| **Expose port 800x ke publik** | ❌ Jangan | Bahaya, tutup via firewall (UFW) |
| **Nginx handle semua** | ✅ WAJIB | Nginx jadi "satpam" (Gatekeeper) |

**Upgrade ke Production Grade:**
1.  **Gunicorn/Uvicorn**: Pengganti `manage.py runserver` untuk performa stabil.
    *   `gunicorn app1.wsgi:application --bind 127.0.0.1:8001`
2.  **Supervisor / Systemd**: Agar kalau VM restart, Django nyala sendiri otomatis.
3.  **Docker (Opsional)**: Untuk isolasi yang lebih rapi lagi.

Jika butuh arsitektur yang lebih kompleks (Load Balancing, Docker Swarm, dll), silakan kontak lagi!
