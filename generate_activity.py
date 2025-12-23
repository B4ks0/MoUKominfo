import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Polygon, Ellipse
import numpy as np

# Set style
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 12

print("Generating CLEAN Activity Diagram (Fixed Arrows)...")

# PORTRAIT: taller than wide
fig, ax = plt.subplots(figsize=(12, 18))
ax.set_xlim(0, 12)
ax.set_ylim(0, 18)
ax.axis('off')

# ============================================================
# Swimlanes
# ============================================================
# Vertical line separator
ax.axvline(x=6, ymin=0.05, ymax=0.95, color='#7f8c8d', linestyle='--', linewidth=2.5, alpha=0.5)

# Swimlane headers
ax.text(3, 17.5, 'Wartawan', ha='center', fontsize=18, fontweight='bold', 
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#3498db', alpha=0.3, edgecolor='#3498db', linewidth=2.5))
ax.text(9, 17.5, 'Sistem', ha='center', fontsize=18, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.5', facecolor='#27ae60', alpha=0.3, edgecolor='#27ae60', linewidth=2.5))

y_pos = 16.5

# ============================================================
# Start
# ============================================================
start = Ellipse((3, y_pos), 0.8, 0.5, facecolor='#2ecc71', edgecolor='black', linewidth=3)
ax.add_patch(start)
ax.text(3, y_pos, 'Start', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1

# Arrow
ax.arrow(3, y_pos+0.6, 0, -0.4, head_width=0.25, head_length=0.15, fc='black', ec='black', linewidth=2.5)
y_pos -= 0.6

# ============================================================
# Activity 1: Akses Portal
# ============================================================
box1 = FancyBboxPatch((1.5, y_pos-0.4), 3, 0.8, boxstyle="round,pad=0.1", 
                       edgecolor='#3498db', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(box1)
ax.text(3, y_pos, 'Akses Portal\nWartawan', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.2

# Arrow to system
ax.arrow(3, y_pos+0.5, 0, -0.3, head_width=0.25, head_length=0.15, fc='black', ec='black', linewidth=2.5)
ax.arrow(3, y_pos+0.2, 5.5, 0, head_width=0.15, head_length=0.25, fc='black', ec='black', linewidth=2.5)
y_pos -= 0.5

# ============================================================
# Activity 2: Tampilkan Form (SAVE Y POSITION FOR LOOP)
# ============================================================
form_y = y_pos  # Save this for the loop back
box2 = FancyBboxPatch((7.5, y_pos-0.4), 3, 0.8, boxstyle="round,pad=0.1", 
                       edgecolor='#27ae60', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(box2)
ax.text(9, y_pos, 'Tampilkan Form\nPendaftaran', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.2

# Arrow back to wartawan
ax.arrow(9, y_pos+0.5, 0, -0.3, head_width=0.25, head_length=0.15, fc='black', ec='black', linewidth=2.5)
ax.arrow(9, y_pos+0.2, -5.5, 0, head_width=0.15, head_length=0.25, fc='black', ec='black', linewidth=2.5)
y_pos -= 0.5

# ============================================================
# Activity 3: Isi Data
# ============================================================
box3 = FancyBboxPatch((1.5, y_pos-0.4), 3, 0.8, boxstyle="round,pad=0.1", 
                       edgecolor='#3498db', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(box3)
ax.text(3, y_pos, 'Isi Data Pribadi\n& Upload Dokumen', ha='center', va='center', fontsize=12, fontweight='bold')
y_pos -= 1.2

# Arrow
ax.arrow(3, y_pos+0.5, 0, -0.3, head_width=0.25, head_length=0.15, fc='black', ec='black', linewidth=2.5)
y_pos -= 0.5

# ============================================================
# Activity 4: Submit
# ============================================================
box4 = FancyBboxPatch((1.5, y_pos-0.4), 3, 0.8, boxstyle="round,pad=0.1", 
                       edgecolor='#3498db', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(box4)
ax.text(3, y_pos, 'Submit\nPendaftaran', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.2

# Arrow to system
ax.arrow(3, y_pos+0.5, 0, -0.3, head_width=0.25, head_length=0.15, fc='black', ec='black', linewidth=2.5)
ax.arrow(3, y_pos+0.2, 5.5, 0, head_width=0.15, head_length=0.25, fc='black', ec='black', linewidth=2.5)
y_pos -= 0.5

# ============================================================
# Decision: Validasi
# ============================================================
diamond_x = 9
diamond_y = y_pos
diamond = Polygon([[diamond_x, diamond_y+0.6], [diamond_x+0.7, diamond_y], 
                   [diamond_x, diamond_y-0.6], [diamond_x-0.7, diamond_y]], 
                  facecolor='#f39c12', edgecolor='black', linewidth=3)
ax.add_patch(diamond)
ax.text(diamond_x, diamond_y, 'Data\nValid?', ha='center', va='center', fontsize=13, fontweight='bold')

# No - LOOP BACK through RIGHT SIDE (avoiding boxes)
# Path: diamond -> right -> up -> left -> form
loop_x_right = 11.5  # Far right, outside all boxes
ax.text(9.8, diamond_y+0.3, 'Tidak', fontsize=12, color='red', fontweight='bold')

# Segment 1: Diamond -> Right
ax.arrow(diamond_x+0.7, diamond_y, 1.8, 0, 
         head_width=0, head_length=0, fc='red', ec='red', linewidth=2.5)

# Segment 2: Right -> Up (to form level)
ax.arrow(loop_x_right, diamond_y, 0, form_y - diamond_y - 0.4,
         head_width=0, head_length=0, fc='red', ec='red', linewidth=2.5)

# Segment 3: Up -> Left (to form box)
ax.arrow(loop_x_right, form_y, -(loop_x_right - 10.5), 0,
         head_width=0.15, head_length=0.25, fc='red', ec='red', linewidth=2.5)

y_pos -= 1.5

# Yes - continue
ax.text(9.5, diamond_y-0.8, 'Ya', fontsize=12, color='green', fontweight='bold')
ax.arrow(diamond_x, diamond_y-0.6, 0, -0.3, head_width=0.25, head_length=0.15, fc='black', ec='black', linewidth=2.5)
y_pos -= 0.5

# ============================================================
# Activity 5: Simpan Data
# ============================================================
box5 = FancyBboxPatch((7.5, y_pos-0.4), 3, 0.8, boxstyle="round,pad=0.1", 
                       edgecolor='#27ae60', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(box5)
ax.text(9, y_pos, 'Simpan Data\nke Database', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.2

# Arrow
ax.arrow(9, y_pos+0.5, 0, -0.3, head_width=0.25, head_length=0.15, fc='black', ec='black', linewidth=2.5)
y_pos -= 0.5

# ============================================================
# Activity 6: Set Status Pending
# ============================================================
box6 = FancyBboxPatch((7.5, y_pos-0.4), 3, 0.8, boxstyle="round,pad=0.1", 
                       edgecolor='#27ae60', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(box6)
ax.text(9, y_pos, 'Set Status:\nPending', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.2

# Arrow
ax.arrow(9, y_pos+0.5, 0, -0.3, head_width=0.25, head_length=0.15, fc='black', ec='black', linewidth=2.5)
y_pos -= 0.5

# ============================================================
# Activity 7: Kirim Notifikasi
# ============================================================
box7 = FancyBboxPatch((7.5, y_pos-0.4), 3, 0.8, boxstyle="round,pad=0.1", 
                       edgecolor='#27ae60', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(box7)
ax.text(9, y_pos, 'Kirim Notifikasi\nBerhasil', ha='center', va='center', fontsize=13, fontweight='bold')
y_pos -= 1.2

# Arrow back to wartawan
ax.arrow(9, y_pos+0.5, 0, -0.3, head_width=0.25, head_length=0.15, fc='black', ec='black', linewidth=2.5)
ax.arrow(9, y_pos+0.2, -5.5, 0, head_width=0.15, head_length=0.25, fc='black', ec='black', linewidth=2.5)
y_pos -= 0.5

# ============================================================
# Activity 8: Terima Konfirmasi
# ============================================================
box8 = FancyBboxPatch((1.5, y_pos-0.4), 3, 0.8, boxstyle="round,pad=0.1", 
                       edgecolor='#3498db', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(box8)
ax.text(3, y_pos, 'Terima Konfirmasi\nPendaftaran', ha='center', va='center', fontsize=12, fontweight='bold')
y_pos -= 1.2

# Arrow to end
ax.arrow(3, y_pos+0.5, 0, -0.4, head_width=0.25, head_length=0.15, fc='black', ec='black', linewidth=2.5)
y_pos -= 0.7

# ============================================================
# End
# ============================================================
end_outer = Ellipse((3, y_pos), 0.8, 0.5, facecolor='white', edgecolor='black', linewidth=3)
end_inner = Ellipse((3, y_pos), 0.6, 0.37, facecolor='#e74c3c', edgecolor='black', linewidth=3)
ax.add_patch(end_outer)
ax.add_patch(end_inner)
ax.text(3, y_pos-0.7, 'End', ha='center', fontsize=13, fontweight='bold')

plt.tight_layout()
plt.savefig('activity_diagram_new.jpg', dpi=400, bbox_inches='tight', pad_inches=0.2)
print("[OK] CLEAN Activity Diagram saved (Fixed arrows)!")
plt.close()

print("\n" + "="*60)
print("[OK] ACTIVITY DIAGRAM FIXED!")
print("="*60)
print("\nFixes Applied:")
print("- Red 'Tidak' arrow now goes through RIGHT side")
print("- Loop path: Diamond -> Right (x=11.5) -> Up -> Left -> Form")
print("- NO overlap with 'Tampilkan Form' box")
print("- Clean, professional flow")
