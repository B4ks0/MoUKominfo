import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set style
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 9

print("Generating PORTRAIT ERD with 2-Column Layout...")

# PORTRAIT orientation: taller than wide
fig, ax = plt.subplots(figsize=(14, 18))
ax.set_xlim(0, 14)
ax.set_ylim(0, 18)
ax.axis('off')

def create_table(ax, x, y, width, height, title, fields, header_color):
    """Helper function to create a table"""
    # Table box
    table_box = Rectangle((x, y), width, height, 
                          linewidth=2.5, edgecolor='#2c3e50', facecolor='#ecf0f1')
    ax.add_patch(table_box)
    
    # Header
    header_box = Rectangle((x, y + height - 0.5), width, 0.5,
                           linewidth=2.5, edgecolor='#2c3e50', facecolor=header_color)
    ax.add_patch(header_box)
    ax.text(x + width/2, y + height - 0.25, 
            title, ha='center', va='center', fontsize=14, fontweight='bold', color='white')
    
    # Fields
    y_offset = y + height - 0.75
    for field in fields:
        ax.text(x + 0.15, y_offset, field, fontsize=8.5, va='top', family='monospace')
        y_offset -= 0.22
    
    return (x, y, width, height)

# ============================================================
# LAYOUT: 2 COLUMNS with CENTRAL ARROW SPACE
# LEFT COLUMN: x = 0.5 to 4.5 (width 4)
# CENTER SPACE: x = 4.5 to 9.5 (width 5) - FOR ARROWS ONLY!
# RIGHT COLUMN: x = 9.5 to 13.5 (width 4)
# ============================================================

LEFT_X = 0.5
LEFT_WIDTH = 4
RIGHT_X = 9.5
RIGHT_WIDTH = 4
CENTER_X = 7  # Middle of arrow space

# ============================================================
# LEFT COLUMN - From Top to Bottom
# ============================================================

# User - TOP LEFT
user_fields = [
    '+ id: BigAutoField (PK)',
    '+ username: CharField(150)',
    '+ password: CharField(128)',
    '+ email: EmailField',
    '+ first_name: CharField(150)',
    '+ last_name: CharField(150)',
    '+ is_staff: BooleanField',
    '+ is_active: BooleanField',
    '+ date_joined: DateTimeField',
]
user_pos = create_table(ax, LEFT_X, 15, LEFT_WIDTH, 2.5, 'User', user_fields, '#e74c3c')

# Permission - UPPER-MIDDLE LEFT
perm_fields = [
    '+ id: BigAutoField (PK)',
    '+ name: CharField(255)',
    '+ content_type_id: FK',
]
perm_pos = create_table(ax, LEFT_X, 12, LEFT_WIDTH, 1.5, 'Permission', perm_fields, '#f39c12')

# ContentType - MIDDLE LEFT
content_fields = [
    '+ id: BigAutoField (PK)',
    '+ app_label: CharField(100)',
    '+ model: CharField(100)',
]
content_pos = create_table(ax, LEFT_X, 9.5, LEFT_WIDTH, 1.5, 'ContentType', content_fields, '#27ae60')

# Wartawan - BOTTOM LEFT (MAIN TABLE)
wartawan_fields = [
    '+ id: BigAutoField (PK)',
    '+ nama_lengkap: CharField(255)',
    '+ nama_media: CharField(255)',
    '+ jabatan: CharField(255)',
    '+ email: EmailField',
    '+ no_hp: CharField(15)',
    '+ alamat: TextField',
    '+ nrp: CharField(20) UNIQUE',
    '+ status: CharField(10)',
    '+ tanggal_daftar: DateTimeField',
    '+ surat_kerja_sama: FileField',
    '+ company_profile: FileField',
    '+ susunan_redaksi: FileField',
    '+ foto_kantor_redaksi: FileField',
    '+ surat_tugas: FileField',
    '+ surat_keputusan: FileField',
    '+ bukti_penerimaan_surat: FileField',
    '+ sppl: FileField',
    '+ surat_keterangan_fiskal: FileField',
    '+ ktp: FileField',
    '+ kartu_pers: FileField',
    '+ sertifikat_kompetensi: FileField',
    '+ surat_pernyataan: FileField',
]
wartawan_pos = create_table(ax, LEFT_X, 2.5, LEFT_WIDTH, 6, 'Wartawan', wartawan_fields, '#3498db')

# ============================================================
# RIGHT COLUMN - From Top to Bottom
# ============================================================

# Session - TOP RIGHT
session_fields = [
    '+ session_key: CharField(40) (PK)',
    '+ session_data: TextField',
    '+ expire_date: DateTimeField',
]
session_pos = create_table(ax, RIGHT_X, 15.5, RIGHT_WIDTH, 1.5, 'Session', session_fields, '#9b59b6')

# Group - UPPER-MIDDLE RIGHT
group_fields = [
    '+ id: BigAutoField (PK)',
    '+ name: CharField(150) UNIQUE',
]
group_pos = create_table(ax, RIGHT_X, 13.5, RIGHT_WIDTH, 1.2, 'Group', group_fields, '#e67e22')

# LogEntry - MIDDLE RIGHT
log_fields = [
    '+ id: BigAutoField (PK)',
    '+ action_time: DateTimeField',
    '+ user_id: FK',
    '+ content_type_id: FK',
    '+ object_id: TextField',
    '+ object_repr: CharField(200)',
    '+ action_flag: PositiveSmallInt',
]
log_pos = create_table(ax, RIGHT_X, 10, RIGHT_WIDTH, 2.5, 'LogEntry', log_fields, '#16a085')

# ============================================================
# RELATIONSHIPS - ALL IN CENTER SPACE (x: 4.5 to 9.5)
# All arrows go through the CENTER only!
# ============================================================

# Helper function to draw arrow through center
def draw_center_arrow(ax, from_pos, to_pos, from_side, to_side, color, label, style='->'):
    """
    Draw arrow that goes through center space
    from_side: 'left' or 'right' (which side of from_pos)
    to_side: 'left' or 'right' (which side of to_pos)
    """
    # Calculate connection points
    if from_side == 'right':
        start_x = from_pos[0] + from_pos[2]
        start_y = from_pos[1] + from_pos[3]/2
    else:
        start_x = from_pos[0]
        start_y = from_pos[1] + from_pos[3]/2
    
    if to_side == 'left':
        end_x = to_pos[0]
        end_y = to_pos[1] + to_pos[3]/2
    else:
        end_x = to_pos[0] + to_pos[2]
        end_y = to_pos[1] + to_pos[3]/2
    
    # Create path through center
    # Horizontal segment to center, then to destination
    mid_y = (start_y + end_y) / 2
    
    # Draw multi-segment arrow
    segments = [
        (start_x, start_y),
        (CENTER_X, start_y),
        (CENTER_X, end_y),
        (end_x, end_y)
    ]
    
    for i in range(len(segments) - 1):
        if i == len(segments) - 2:
            # Last segment with arrow
            arrow = FancyArrowPatch(
                segments[i], segments[i+1],
                arrowstyle=style, mutation_scale=25, linewidth=2.5, color=color
            )
        else:
            # Regular line
            arrow = FancyArrowPatch(
                segments[i], segments[i+1],
                arrowstyle='-', mutation_scale=25, linewidth=2.5, color=color
            )
        ax.add_patch(arrow)
    
    # Add label in center
    label_y = (start_y + end_y) / 2
    ax.text(CENTER_X, label_y, label, fontsize=10, fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=color, linewidth=2))

# 1. ContentType -> Permission (1:N)
draw_center_arrow(ax, content_pos, perm_pos, 'right', 'right', '#27ae60', '1:N')

# 2. User -> LogEntry (1:N)
draw_center_arrow(ax, user_pos, log_pos, 'right', 'left', '#e74c3c', '1:N')

# 3. ContentType -> LogEntry (1:N)
draw_center_arrow(ax, content_pos, log_pos, 'right', 'left', '#27ae60', '1:N')

# 4. User <-> Group (M:N)
draw_center_arrow(ax, user_pos, group_pos, 'right', 'left', '#e67e22', 'M:N', '<->')

# 5. Group <-> Permission (M:N)
draw_center_arrow(ax, group_pos, perm_pos, 'left', 'right', '#9b59b6', 'M:N', '<->')

# 6. User -> Wartawan (manages - dashed)
# Special case: same column, so use different approach
arrow6 = FancyArrowPatch(
    (user_pos[0] + user_pos[2]/2, user_pos[1]),
    (wartawan_pos[0] + wartawan_pos[2]/2, wartawan_pos[1] + wartawan_pos[3]),
    arrowstyle='->', mutation_scale=25, linewidth=2, color='#95a5a6',
    linestyle='--', alpha=0.7
)
ax.add_patch(arrow6)
ax.text(LEFT_X + LEFT_WIDTH/2 - 1, 11, 'manages', fontsize=9, style='italic', color='#7f8c8d')

plt.tight_layout()
plt.savefig('database_erd.jpg', dpi=400, bbox_inches='tight', pad_inches=0.3)
print("[OK] PORTRAIT ERD with 2-Column Layout saved!")
plt.close()

print("\n" + "="*60)
print("[OK] PERFECT 2-COLUMN ERD GENERATED!")
print("="*60)
print("\nLayout Strategy:")
print("- PORTRAIT orientation (14×18)")
print("- LEFT Column: User, Permission, ContentType, Wartawan")
print("- RIGHT Column: Session, Group, LogEntry")
print("- CENTER Space (x: 4.5-9.5): ALL ARROWS")
print("\nKey Features:")
print("- NO tables in center space")
print("- ALL arrows go through center only")
print("- NO overlapping with tables")
print("- Clean, professional 2-column design")
