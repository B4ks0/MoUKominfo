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
