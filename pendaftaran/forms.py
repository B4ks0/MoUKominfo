from django import forms
from captcha.fields import CaptchaField
from .models import Wartawan

class WartawanForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Wartawan
        fields = [
            'nama_lengkap', 'nama_media', 'jabatan', 'email', 'no_hp', 'alamat',
            'surat_kerja_sama', 'company_profile', 'susunan_redaksi', 'foto_kantor_redaksi',
            'surat_tugas', 'surat_keputusan', 'bukti_penerimaan_surat', 'sppl',
            'surat_keterangan_fiskal', 'ktp', 'kartu_pers', 'sertifikat_kompetensi', 'surat_pernyataan'
        ]
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control'}),
            'nama_media': forms.TextInput(attrs={'class': 'form-control'}),
            'jabatan': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'no_hp': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.FileField):
                field.required = False  # Make file fields optional as per description

class StatusCheckForm(forms.Form):
    nrp = forms.CharField(label='Nomor Permohonan (NRP)', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukkan NRP Anda'}))
    captcha = CaptchaField()
