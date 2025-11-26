from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import WartawanForm
from .models import Wartawan

def index(request):
    return render(request, 'pendaftaran/index.html')

def register(request):
    if request.method == 'POST':
        form = WartawanForm(request.POST, request.FILES)
        if form.is_valid():
            wartawan = form.save()
            messages.success(request, f'Pendaftaran berhasil! Nomor Registrasi Permohonan (NRP) Anda: {wartawan.nrp}. Status Anda sedang menunggu verifikasi.')
            return redirect('pendaftaran:index')
    else:
        form = WartawanForm()
    return render(request, 'pendaftaran/register.html', {'form': form})

def check_status(request):
    status_result = None
    if request.method == 'POST':
        nrp = request.POST.get('nrp')
        if nrp:
            try:
                wartawan = Wartawan.objects.get(nrp=nrp)
                status_result = {
                    'nrp': nrp,
                    'status': dict(Wartawan.STATUS_CHOICES).get(wartawan.status, wartawan.status),
                    'nama': wartawan.nama_lengkap,
                    'tanggal': wartawan.tanggal_daftar.strftime('%d %B %Y')
                }
            except Wartawan.DoesNotExist:
                messages.error(request, 'NRP tidak ditemukan.')
    return render(request, 'pendaftaran/check_status.html', {'status_result': status_result})
