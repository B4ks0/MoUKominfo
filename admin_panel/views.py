from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST
from pendaftaran.models import Wartawan
from django.http import HttpResponse
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def staff_required(user):
    return user.is_staff

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, 'Login berhasil! Selamat datang di Admin Panel.')
            return redirect('admin_panel:dashboard')
        else:
            messages.error(request, 'Username atau password salah.')
    return render(request, 'admin_panel/login.html')

@login_required
@user_passes_test(staff_required)
def dashboard(request):
    total = Wartawan.objects.count()
    pending = Wartawan.objects.filter(status='pending').count()
    approved = Wartawan.objects.filter(status='approved').count()
    rejected = Wartawan.objects.filter(status='rejected').count()
    latest_wartawan = Wartawan.objects.order_by('-tanggal_daftar')[:5]
    context = {
        'total': total,
        'pending': pending,
        'approved': approved,
        'rejected': rejected,
        'latest_wartawan': latest_wartawan,
    }
    return render(request, 'admin_panel/dashboard.html', context)

@login_required
@user_passes_test(staff_required)
def manage(request):
    status_filter = request.GET.get('status', '')
    search_query = request.GET.get('search', '')
    wartawans = Wartawan.objects.all().order_by('-tanggal_daftar')
    if status_filter:
        wartawans = wartawans.filter(status=status_filter)
    if search_query:
        wartawans = wartawans.filter(
            nama_lengkap__icontains=search_query
        ) | wartawans.filter(
            nama_media__icontains=search_query
        ) | wartawans.filter(
            email__icontains=search_query
        ) | wartawans.filter(
            jabatan__icontains=search_query
        )
    paginator = Paginator(wartawans, 10)  # Show 10 wartawans per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'status_filter': status_filter,
        'search_query': search_query,
    }
    return render(request, 'admin_panel/manage.html', context)

@login_required
@user_passes_test(staff_required)
def verify(request, pk):
    wartawan = get_object_or_404(Wartawan, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['pending', 'approved', 'rejected']:
            wartawan.status = new_status
            wartawan.save()
            messages.success(request, f'Status {wartawan.nama_lengkap} telah diubah menjadi {new_status}.')
            return redirect(reverse('admin_panel:verify', args=[pk]))
    return render(request, 'admin_panel/verify.html', {'wartawan': wartawan})

@login_required
@user_passes_test(staff_required)
def delete_wartawan(request, pk):
    wartawan = get_object_or_404(Wartawan, pk=pk)
    wartawan.delete()
    messages.success(request, 'Data wartawan berhasil dihapus.')
    return redirect(reverse('admin_panel:manage'))

@login_required
@user_passes_test(staff_required)
def report(request):
    if request.GET.get('export') == 'csv':
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="laporan_wartawan.csv"'
        writer = csv.writer(response)
        writer.writerow([
            'Nomor Permohonan', 'Nama Lengkap', 'Nama Media', 'Jabatan', 'Email', 'No HP',
            'Alamat', 'Status', 'Tanggal Daftar'
        ])
        wartawans = Wartawan.objects.all().order_by('-tanggal_daftar')
        for w in wartawans:
            writer.writerow([
                w.nrp, w.nama_lengkap, w.nama_media, w.jabatan,
                w.email, w.no_hp, w.alamat, w.status, w.tanggal_daftar
            ])
        return response
    wartawans = Wartawan.objects.all().order_by('-tanggal_daftar')
    paginator = Paginator(wartawans, 10)  # Show 10 wartawans per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_panel/report.html', {'page_obj': page_obj})

@login_required
@user_passes_test(staff_required)
def logout_view(request):
    logout(request)
    return redirect('pendaftaran:index')

@login_required
@user_passes_test(staff_required)
def auto_verify(request):
    if request.method == 'POST':
        # Simple auto-verify: approve all pending
        count = Wartawan.objects.filter(status='pending').update(status='approved')
        messages.success(request, f'{count} pendaftaran pending telah disetujui.')
        return redirect(reverse('admin_panel:auto_verify'))
    pending_wartawans = Wartawan.objects.filter(status='pending').order_by('-tanggal_daftar')
    paginator = Paginator(pending_wartawans, 10)  # Show 10 pending wartawans per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'pending_count': pending_wartawans.count()
    }
    return render(request, 'admin_panel/auto_verify.html', context)
