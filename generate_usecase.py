import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse, Rectangle, Polygon
import numpy as np

# Set style
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 11

print("Generating PORTRAIT Use Case Diagram (Clean)...")

# PORTRAIT: taller than wide
fig, ax = plt.subplots(figsize=(12, 16))
ax.set_xlim(0, 12)
ax.set_ylim(0, 16)
ax.axis('off')

# ============================================================
# System boundary
# ============================================================
system_box = Rectangle((2.5, 2), 7, 11.5, linewidth=3, 
                        edgecolor='#2c3e50', facecolor='none', linestyle='--')
ax.add_patch(system_box)
ax.text(6, 13.2, 'Sistem Pendaftaran Online Wartawan', 
        ha='center', fontsize=16, fontweight='bold', style='italic', color='#2c3e50')

# ============================================================
# Actors
# ============================================================

def draw_actor(ax, x, y, name, color):
    """Draw stick figure actor"""
    # Head
    head = Ellipse((x, y), 0.5, 0.6, facecolor=color, edgecolor='black', linewidth=2.5)
    ax.add_patch(head)
    
    # Body
    body = Rectangle((x-0.2, y-1.2), 0.4, 1.2, facecolor=color, edgecolor='black', linewidth=2.5)
    ax.add_patch(body)
    
    # Arms
    ax.plot([x-0.5, x-0.7], [y-0.5, y-1.0], 'k-', linewidth=3)
    ax.plot([x+0.5, x+0.7], [y-0.5, y-1.0], 'k-', linewidth=3)
    
    # Legs
    ax.plot([x-0.2, x-0.5], [y-1.2, y-2.0], 'k-', linewidth=3)
    ax.plot([x+0.2, x+0.5], [y-1.2, y-2.0], 'k-', linewidth=3)
    
    # Name
    ax.text(x, y-2.5, name, ha='center', fontsize=14, fontweight='bold')

# Wartawan - LEFT
draw_actor(ax, 1.2, 10, 'Wartawan', '#3498db')

# Admin - RIGHT
draw_actor(ax, 10.8, 10, 'Admin\nKominfo', '#e74c3c')

# ============================================================
# Use Cases - Wartawan side (LEFT)
# ============================================================
use_cases_wartawan = [
    (4.5, 11.5, 'Lihat Informasi\nPortal'),
    (4.5, 9.8, 'Daftar Akun\nBaru'),
    (4.5, 8.1, 'Upload\nDokumen'),
    (4.5, 6.4, 'Cek Status\nPendaftaran'),
]

for x, y, label in use_cases_wartawan:
    ellipse = Ellipse((x, y), 2.2, 1.0, facecolor='#ecf0f1', 
                      edgecolor='#3498db', linewidth=3)
    ax.add_patch(ellipse)
    ax.text(x, y, label, ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Connect to Wartawan
    ax.plot([1.7, x-1.1], [9, y], 'k-', linewidth=2, alpha=0.6)

# ============================================================
# Use Cases - Admin side (RIGHT)
# ============================================================
use_cases_admin = [
    (7.5, 11.5, 'Login\nAdmin'),
    (7.5, 10.2, 'Lihat\nDashboard'),
    (7.5, 8.9, 'Verifikasi\nPendaftaran'),
    (7.5, 7.6, 'Kelola Data\nWartawan'),
    (7.5, 6.3, 'Generate\nLaporan'),
    (7.5, 5.0, 'Kelola\nPermissions'),
]

for x, y, label in use_cases_admin:
    ellipse = Ellipse((x, y), 2.2, 1.0, facecolor='#ecf0f1', 
                      edgecolor='#e74c3c', linewidth=3)
    ax.add_patch(ellipse)
    ax.text(x, y, label, ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Connect to Admin
    ax.plot([10.3, x+1.1], [9, y], 'k-', linewidth=2, alpha=0.6)

# ============================================================
# Central use case (shared/system)
# ============================================================
central_uc = Ellipse((6, 3.5), 2.5, 1.2, facecolor='#f39c12', 
                     edgecolor='#2c3e50', linewidth=3.5)
ax.add_patch(central_uc)
ax.text(6, 3.5, 'Database\nManagement', ha='center', va='center', 
        fontsize=13, fontweight='bold', color='white')

# Connect central to both sides
ax.plot([5.6, 6-1.25], [6.4, 4.1], 'k--', linewidth=2, alpha=0.5)
ax.plot([8.4, 6+1.25], [6.3, 4.1], 'k--', linewidth=2, alpha=0.5)

# ============================================================
# Include relationships (dashed arrows between use cases)
# ============================================================

# Upload Dokumen includes Daftar Akun
include1 = FancyArrowPatch((4.5, 8.6), (4.5, 9.3),
                           arrowstyle='->', mutation_scale=20, linewidth=1.5, 
                           color='#95a5a6', linestyle=':')
ax.add_patch(include1)
ax.text(5.2, 8.95, '«include»', fontsize=9, style='italic', color='#7f8c8d')

# Verifikasi includes Lihat Dashboard
include2 = FancyArrowPatch((7.5, 9.4), (7.5, 9.7),
                           arrowstyle='->', mutation_scale=20, linewidth=1.5, 
                           color='#95a5a6', linestyle=':')
ax.add_patch(include2)
ax.text(8.2, 9.55, '«include»', fontsize=9, style='italic', color='#7f8c8d')

plt.tight_layout()
plt.savefig('usecase_diagram_new.jpg', dpi=400, bbox_inches='tight', pad_inches=0.2)
print("[OK] PORTRAIT Use Case Diagram saved!")
plt.close()

print("\n" + "="*60)
print("[OK] CLEAN USE CASE DIAGRAM GENERATED!")
print("="*60)
print("\nFeatures:")
print("- PORTRAIT orientation (12×16)")
print("- NO title at top")
print("- NO legend at bottom")
print("- LARGER actors and use cases")
print("- 2 actors: Wartawan (left), Admin (right)")
print("- 10 use cases total")
print("- System boundary clearly defined")
print("- Include relationships shown")
print("- Clean, professional design")
