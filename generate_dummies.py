import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MoUKominfo.settings')
import django
django.setup()

from pendaftaran.models import Wartawan
from datetime import date
import random

today = date.today().strftime('%Y%m%d')
names = ['Ahmad Santoso', 'Siti Nurhaliza', 'Budi Hartono', 'Dewi Sartika', 'Eko Prasetyo', 'Fitriani Rahman', 'Gatot Subroto', 'Hani Wijaya', 'Indra Kurniawan', 'Joko Widodo', 'Kartika Sari', 'Larasati Putri', 'Muhammad Ali', 'Nadia Pratiwi', 'Oscar Nugroho', 'Purnama Sari', 'Qori Andini', 'Rina Susanti', 'Surya Pratama', 'Tina Melati', 'Umar Faruq', 'Vina Citra', 'Wahyu Setiawan', 'Xena Lestari', 'Yudi Hermawan', 'Zara Amelia']
media = ['Kompas', 'Tempo', 'Detik', 'CNN Indonesia', 'Tribun', 'Liputan6', 'Okezone', 'Suara', 'Viva', 'Sindo']
jabatan = ['Reporter', 'Editor', 'Fotografer', 'Koresponden', 'Penulis']
emails = ['ahmad@kompas.com', 'siti@tempo.co', 'budi@detik.com', 'dewi@cnnindonesia.com', 'eko@tribunnews.com', 'fitri@liputan6.com', 'gatot@okezone.com', 'hani@suara.com', 'indra@viva.co.id', 'joko@sindonews.com', 'kartika@kompas.com', 'laras@tempo.co', 'muhammad@detik.com', 'nadia@cnnindonesia.com', 'oscar@tribunnews.com', 'purnama@liputan6.com', 'qori@okezone.com', 'rina@suara.com', 'surya@viva.co.id', 'tina@sindonews.com', 'umar@kompas.com', 'vina@tempo.co', 'wahyu@detik.com', 'xena@cnnindonesia.com', 'yudi@tribunnews.com', 'zara@liputan6.com']
no_hp = ['081234567890', '081234567891', '081234567892', '081234567893', '081234567894', '081234567895', '081234567896', '081234567897', '081234567898', '081234567899', '082345678901', '082345678902', '082345678903', '082345678904', '082345678905', '082345678906', '082345678907', '082345678908', '082345678909', '082345678910', '083456789011', '083456789012', '083456789013', '083456789014', '083456789015']
alamat = ['Jl. Merdeka No.1, Manado', 'Jl. Sudirman No.2, Minahasa', 'Jl. Gatot Subroto No.3, Tondano', 'Jl. Ahmad Yani No.4, Tomohon', 'Jl. Raya Pineleng No.5, Airmadidi']
statuses = ['pending', 'approved', 'rejected']

for i in range(100):
    w = Wartawan(
        nama_lengkap=random.choice(names),
        nama_media=random.choice(media),
        jabatan=random.choice(jabatan),
        email=random.choice(emails),
        no_hp=random.choice(no_hp),
        alamat=random.choice(alamat),
        status=random.choice(statuses)
    )
    w.save()
    print(f'Created {i+1}: NRP {w.nrp}, Status: {w.status}')
