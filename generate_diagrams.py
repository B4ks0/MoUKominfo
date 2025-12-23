import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse, Rectangle, Polygon
import numpy as np

# Set style with LARGER fonts
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 14  # Increased from 9

# ============================================================
# DIAGRAM 1: USE CASE DIAGRAM - LARGER VERSION
# ============================================================
print("Generating LARGER Use Case Diagram...")

fig, ax = plt.subplots(figsize=(16, 12))  # Increased from (14, 10)
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.axis('off')

# Title - LARGER
ax.text(7, 9.7, 'Use Case Diagram', 
        ha='center', fontsize=20, fontweight='bold')
ax.text(7, 9.3, 'Sistem Pendaftaran Wartawan Online', 
        ha='center', fontsize=16, style='italic')

# System boundary - THICKER
system_box = Rectangle((3, 0.5), 8, 8, linewidth=3, 
                        edgecolor='#2c3e50', facecolor='none', linestyle='--')
ax.add_patch(system_box)
ax.text(7, 8.3, 'Sistem Pendaftaran Online', 
        ha='center', fontsize=14, fontweight='bold', style='italic')

# Actors - LARGER
# Wartawan (left) - BIGGER
wartawan_head = Ellipse((1.5, 7), 0.4, 0.5, facecolor='#3498db', edgecolor='black', linewidth=2)
wartawan_body = Rectangle((1.3, 6.2), 0.4, 0.8, facecolor='#3498db', edgecolor='black', linewidth=2)
ax.add_patch(wartawan_head)
ax.add_patch(wartawan_body)
ax.plot([1.1, 0.9], [6.5, 5.9], 'k-', linewidth=2.5)  # left arm
ax.plot([1.9, 2.1], [6.5, 5.9], 'k-', linewidth=2.5)  # right arm
ax.plot([1.3, 1.0], [6.2, 5.3], 'k-', linewidth=2.5)  # left leg
ax.plot([1.7, 2.0], [6.2, 5.3], 'k-', linewidth=2.5)  # right leg
ax.text(1.5, 4.9, 'Wartawan', ha='center', fontsize=16, fontweight='bold')

# Admin (right) - BIGGER
admin_head = Ellipse((12.5, 7), 0.4, 0.5, facecolor='#e74c3c', edgecolor='black', linewidth=2)
admin_body = Rectangle((12.3, 6.2), 0.4, 0.8, facecolor='#e74c3c', edgecolor='black', linewidth=2)
ax.add_patch(admin_head)
ax.add_patch(admin_body)
ax.plot([12.1, 11.9], [6.5, 5.9], 'k-', linewidth=2.5)
ax.plot([12.9, 13.1], [6.5, 5.9], 'k-', linewidth=2.5)
ax.plot([12.3, 12.0], [6.2, 5.3], 'k-', linewidth=2.5)
ax.plot([12.7, 13.0], [6.2, 5.3], 'k-', linewidth=2.5)
ax.text(12.5, 4.9, 'Admin', ha='center', fontsize=16, fontweight='bold')
ax.text(12.5, 4.5, 'Kominfo', ha='center', fontsize=14, fontweight='bold')

# Use Cases - Wartawan side - LARGER ellipses and BIGGER text
use_cases_wartawan = [
    (5, 7.5, 'Lihat Informasi\nPortal'),
    (5, 6.3, 'Daftar Akun\nBaru'),
    (5, 5.1, 'Upload\nDokumen'),
    (5, 3.9, 'Cek Status\nPendaftaran'),
]

for x, y, label in use_cases_wartawan:
    ellipse = Ellipse((x, y), 1.8, 0.75, facecolor='#ecf0f1', 
                      edgecolor='#3498db', linewidth=2.5)
    ax.add_patch(ellipse)
    ax.text(x, y, label, ha='center', va='center', fontsize=12, fontweight='bold')
    # Connect to Wartawan - THICKER
    ax.plot([2.0, x-0.9], [6.5, y], 'k-', linewidth=1.5, alpha=0.7)

# Use Cases - Admin side - LARGER
use_cases_admin = [
    (9, 7.5, 'Login\nAdmin'),
    (9, 6.5, 'Lihat\nDashboard'),
    (9, 5.5, 'Verifikasi\nPendaftaran'),
    (9, 4.5, 'Kelola Data\nWartawan'),
    (9, 3.5, 'Generate\nLaporan'),
]

for x, y, label in use_cases_admin:
    ellipse = Ellipse((x, y), 1.8, 0.75, facecolor='#ecf0f1', 
                      edgecolor='#e74c3c', linewidth=2.5)
    ax.add_patch(ellipse)
    ax.text(x, y, label, ha='center', va='center', fontsize=12, fontweight='bold')
    # Connect to Admin - THICKER
    ax.plot([12.0, x+0.9], [6.5, y], 'k-', linewidth=1.5, alpha=0.7)

# Central use case (shared) - LARGER
central_uc = Ellipse((7, 2.2), 2.0, 0.85, facecolor='#f39c12', 
                     edgecolor='#2c3e50', linewidth=3)
ax.add_patch(central_uc)
ax.text(7, 2.2, 'Database\nManagement', ha='center', va='center', 
        fontsize=13, fontweight='bold')

# Connect central to both actors
ax.plot([5.9, 7-1.0], [3.9, 2.6], 'k--', linewidth=1.5, alpha=0.5)
ax.plot([9.9, 7+1.0], [3.5, 2.6], 'k--', linewidth=1.5, alpha=0.5)

# Legend - LARGER
ax.text(0.5, 1.3, 'Keterangan:', fontsize=14, fontweight='bold')
ax.text(0.5, 0.85, '• Wartawan: Pengguna publik yang mendaftar', fontsize=12)
ax.text(0.5, 0.4, '• Admin: Pengelola sistem dari Kominfo', fontsize=12)

plt.tight_layout()
plt.savefig('usecase_diagram_new.jpg', dpi=400, bbox_inches='tight')  # Increased DPI
print("[OK] Use Case Diagram saved: usecase_diagram_new.jpg (LARGER)")
plt.close()

# ============================================================
# DIAGRAM 2: ACTIVITY DIAGRAM - LARGER VERSION
# ============================================================
print("Generating LARGER Activity Diagram...")

fig, ax = plt.subplots(figsize=(14, 16))  # Increased from (12, 14)
ax.set_xlim(0, 10)
ax.set_ylim(0, 16)
ax.axis('off')

# Title - LARGER
ax.text(5, 15.5, 'Activity Diagram', 
        ha='center', fontsize=22, fontweight='bold')
ax.text(5, 15.0, 'Proses Pendaftaran Wartawan', 
        ha='center', fontsize=17, style='italic')

# Swimlanes - THICKER
ax.axvline(x=5, ymin=0.05, ymax=0.92, color='gray', linestyle='--', linewidth=2.5, alpha=0.6)
ax.text(2.5, 14.5, 'Wartawan', ha='center', fontsize=16, fontweight='bold', 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#3498db', alpha=0.4, edgecolor='black', linewidth=2))
ax.text(7.5, 14.5, 'Sistem', ha='center', fontsize=16, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#27ae60', alpha=0.4, edgecolor='black', linewidth=2))

y_pos = 13.8

# Start - LARGER
start = Ellipse((2.5, y_pos), 0.5, 0.35, facecolor='#2ecc71', edgecolor='black', linewidth=2.5)
ax.add_patch(start)
ax.text(2.5, y_pos, 'Start', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 0.9

# Arrow - THICKER
ax.arrow(2.5, y_pos+0.5, 0, -0.35, head_width=0.2, head_length=0.12, fc='black', ec='black', linewidth=2)
y_pos -= 0.6

# Activity 1: Akses Portal - LARGER BOX
box1 = FancyBboxPatch((1.3, y_pos-0.35), 2.4, 0.7, boxstyle="round,pad=0.08", 
                       edgecolor='#3498db', facecolor='#ecf0f1', linewidth=2.5)
ax.add_patch(box1)
ax.text(2.5, y_pos, 'Akses Portal\nWartawan', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.1

# Arrow to system - THICKER
ax.arrow(2.5, y_pos+0.45, 0, -0.25, head_width=0.2, head_length=0.12, fc='black', ec='black', linewidth=2)
ax.arrow(2.5, y_pos+0.2, 4.5, 0, head_width=0.12, head_length=0.2, fc='black', ec='black', linewidth=2)
y_pos -= 0.4

# Activity 2: Tampilkan Form - LARGER
box2 = FancyBboxPatch((6.3, y_pos-0.35), 2.4, 0.7, boxstyle="round,pad=0.08", 
                       edgecolor='#27ae60', facecolor='#ecf0f1', linewidth=2.5)
ax.add_patch(box2)
ax.text(7.5, y_pos, 'Tampilkan Form\nPendaftaran', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.1

# Arrow back to wartawan - THICKER
ax.arrow(7.5, y_pos+0.45, 0, -0.25, head_width=0.2, head_length=0.12, fc='black', ec='black', linewidth=2)
ax.arrow(7.5, y_pos+0.2, -4.5, 0, head_width=0.12, head_length=0.2, fc='black', ec='black', linewidth=2)
y_pos -= 0.4

# Activity 3: Isi Data - LARGER
box3 = FancyBboxPatch((1.3, y_pos-0.35), 2.4, 0.7, boxstyle="round,pad=0.08", 
                       edgecolor='#3498db', facecolor='#ecf0f1', linewidth=2.5)
ax.add_patch(box3)
ax.text(2.5, y_pos, 'Isi Data Pribadi\n& Upload Dokumen', ha='center', va='center', fontsize=12, fontweight='bold')
y_pos -= 1.1

# Arrow - THICKER
ax.arrow(2.5, y_pos+0.45, 0, -0.25, head_width=0.2, head_length=0.12, fc='black', ec='black', linewidth=2)
y_pos -= 0.4

# Activity 4: Submit - LARGER
box4 = FancyBboxPatch((1.3, y_pos-0.35), 2.4, 0.7, boxstyle="round,pad=0.08", 
                       edgecolor='#3498db', facecolor='#ecf0f1', linewidth=2.5)
ax.add_patch(box4)
ax.text(2.5, y_pos, 'Submit\nPendaftaran', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.1

# Arrow to system - THICKER
ax.arrow(2.5, y_pos+0.45, 0, -0.25, head_width=0.2, head_length=0.12, fc='black', ec='black', linewidth=2)
ax.arrow(2.5, y_pos+0.2, 4.5, 0, head_width=0.12, head_length=0.2, fc='black', ec='black', linewidth=2)
y_pos -= 0.4

# Decision: Validasi - LARGER DIAMOND
diamond_x = 7.5
diamond_y = y_pos
diamond = Polygon([[diamond_x, diamond_y+0.5], [diamond_x+0.6, diamond_y], 
                   [diamond_x, diamond_y-0.5], [diamond_x-0.6, diamond_y]], 
                  facecolor='#f39c12', edgecolor='black', linewidth=2.5)
ax.add_patch(diamond)
ax.text(diamond_x, diamond_y, 'Valid?', ha='center', va='center', fontsize=14, fontweight='bold')
y_pos -= 1.2

# No - back to form - THICKER
ax.text(8.5, diamond_y+0.25, 'Tidak', fontsize=13, color='red', fontweight='bold')
ax.arrow(diamond_x+0.6, diamond_y, 0.9, 0, head_width=0.12, head_length=0.15, fc='red', ec='red', linewidth=2)
ax.arrow(9.0, diamond_y, 0, 4.0, head_width=0.12, head_length=0.15, fc='red', ec='red', linewidth=2)
ax.arrow(9.0, diamond_y+4.0, -1.5, 0, head_width=0.12, head_length=0.15, fc='red', ec='red', linewidth=2)

# Yes - continue - THICKER
ax.text(8.0, diamond_y-0.6, 'Ya', fontsize=13, color='green', fontweight='bold')
ax.arrow(diamond_x, diamond_y-0.5, 0, -0.25, head_width=0.2, head_length=0.12, fc='black', ec='black', linewidth=2)
y_pos -= 0.4

# Activity 5: Simpan Data - LARGER
box5 = FancyBboxPatch((6.3, y_pos-0.35), 2.4, 0.7, boxstyle="round,pad=0.08", 
                       edgecolor='#27ae60', facecolor='#ecf0f1', linewidth=2.5)
ax.add_patch(box5)
ax.text(7.5, y_pos, 'Simpan Data\nke Database', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.1

# Arrow - THICKER
ax.arrow(7.5, y_pos+0.45, 0, -0.25, head_width=0.2, head_length=0.12, fc='black', ec='black', linewidth=2)
y_pos -= 0.4

# Activity 6: Set Status Pending - LARGER
box6 = FancyBboxPatch((6.3, y_pos-0.35), 2.4, 0.7, boxstyle="round,pad=0.08", 
                       edgecolor='#27ae60', facecolor='#ecf0f1', linewidth=2.5)
ax.add_patch(box6)
ax.text(7.5, y_pos, 'Set Status:\nPending', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.1

# Arrow - THICKER
ax.arrow(7.5, y_pos+0.45, 0, -0.25, head_width=0.2, head_length=0.12, fc='black', ec='black', linewidth=2)
y_pos -= 0.4

# Activity 7: Kirim Notifikasi - LARGER
box7 = FancyBboxPatch((6.3, y_pos-0.35), 2.4, 0.7, boxstyle="round,pad=0.08", 
                       edgecolor='#27ae60', facecolor='#ecf0f1', linewidth=2.5)
ax.add_patch(box7)
ax.text(7.5, y_pos, 'Kirim Notifikasi\nBerhasil', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.1

# Arrow back to wartawan - THICKER
ax.arrow(7.5, y_pos+0.45, 0, -0.25, head_width=0.2, head_length=0.12, fc='black', ec='black', linewidth=2)
ax.arrow(7.5, y_pos+0.2, -4.5, 0, head_width=0.12, head_length=0.2, fc='black', ec='black', linewidth=2)
y_pos -= 0.4

# Activity 8: Terima Konfirmasi - LARGER
box8 = FancyBboxPatch((1.3, y_pos-0.35), 2.4, 0.7, boxstyle="round,pad=0.08", 
                       edgecolor='#3498db', facecolor='#ecf0f1', linewidth=2.5)
ax.add_patch(box8)
ax.text(2.5, y_pos, 'Terima Konfirmasi\nPendaftaran', ha='center', va='center', fontsize=12, fontweight='bold')
y_pos -= 1.1

# Arrow to end - THICKER
ax.arrow(2.5, y_pos+0.45, 0, -0.35, head_width=0.2, head_length=0.12, fc='black', ec='black', linewidth=2)
y_pos -= 0.6

# End - LARGER
end_outer = Ellipse((2.5, y_pos), 0.5, 0.35, facecolor='white', edgecolor='black', linewidth=2.5)
end_inner = Ellipse((2.5, y_pos), 0.38, 0.26, facecolor='#e74c3c', edgecolor='black', linewidth=2.5)
ax.add_patch(end_outer)
ax.add_patch(end_inner)
ax.text(2.5, y_pos-0.6, 'End', ha='center', fontsize=13, fontweight='bold')

# Legend - LARGER
ax.text(0.5, 1.6, 'Keterangan:', fontsize=14, fontweight='bold')
ax.text(0.5, 1.2, '• Kotak: Aktivitas/Proses', fontsize=12)
ax.text(0.5, 0.8, '• Belah Ketupat: Keputusan/Validasi', fontsize=12)
ax.text(0.5, 0.4, '• Lingkaran: Start/End', fontsize=12)

plt.tight_layout()
plt.savefig('activity_diagram_new.jpg', dpi=400, bbox_inches='tight')  # Increased DPI
print("[OK] Activity Diagram saved: activity_diagram_new.jpg (LARGER)")
plt.close()

print("\n" + "="*60)
print("[OK] ALL LARGER DIAGRAMS GENERATED SUCCESSFULLY!")
print("="*60)
print("\nGenerated files:")
print("1. usecase_diagram_new.jpg - LARGER Use Case Diagram")
print("2. activity_diagram_new.jpg - LARGER Activity Diagram")
print("\nImprovements:")
print("- Figure size increased by 15-20%")
print("- Font sizes increased from 8-9 to 12-16")
print("- Line widths increased from 1-2 to 2-2.5")
print("- DPI increased from 300 to 400")
print("- All elements (boxes, ellipses, arrows) are BIGGER")
