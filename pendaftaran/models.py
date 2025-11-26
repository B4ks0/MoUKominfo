from django.db import models
from django.core.validators import RegexValidator

class Wartawan(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    nama_lengkap = models.CharField(max_length=255)
    nama_media = models.CharField(max_length=255)
    jabatan = models.CharField(max_length=255)
    email = models.EmailField()
    no_hp = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\d{10,15}$', 'Nomor HP harus 10-15 digit.')]
    )
    alamat = models.TextField()
    nrp = models.CharField(max_length=20, unique=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    tanggal_daftar = models.DateTimeField(auto_now_add=True)

    # File fields for documents
    surat_kerja_sama = models.FileField(upload_to='uploads/', blank=True, null=True)
    company_profile = models.FileField(upload_to='uploads/', blank=True, null=True)
    susunan_redaksi = models.FileField(upload_to='uploads/', blank=True, null=True)
    foto_kantor_redaksi = models.FileField(upload_to='uploads/', blank=True, null=True)
    surat_tugas = models.FileField(upload_to='uploads/', blank=True, null=True)
    surat_keputusan = models.FileField(upload_to='uploads/', blank=True, null=True)
    bukti_penerimaan_surat = models.FileField(upload_to='uploads/', blank=True, null=True)
    sppl = models.FileField(upload_to='uploads/', blank=True, null=True)
    surat_keterangan_fiskal = models.FileField(upload_to='uploads/', blank=True, null=True)
    ktp = models.FileField(upload_to='uploads/', blank=True, null=True)
    kartu_pers = models.FileField(upload_to='uploads/', blank=True, null=True)
    sertifikat_kompetensi = models.FileField(upload_to='uploads/', blank=True, null=True)
    surat_pernyataan = models.FileField(upload_to='uploads/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.nrp:
            from datetime import date
            today = date.today().strftime('%Y%m%d')
            if self.pk:
                self.nrp = f'NRP-{today}-{str(self.pk).zfill(4)}'
            else:
                super().save(*args, **kwargs)  # Save first to get pk
                self.nrp = f'NRP-{today}-{str(self.pk).zfill(4)}'
                super().save(*args, **kwargs)  # Save again with nrp
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.nama_lengkap
