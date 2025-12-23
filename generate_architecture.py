import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
import numpy as np

# Set style
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 12

print("Generating PORTRAIT Architecture Diagram (Clean)...")

# PORTRAIT: taller than wide
fig, ax = plt.subplots(figsize=(12, 16))
ax.set_xlim(0, 12)
ax.set_ylim(0, 16)
ax.axis('off')

# ============================================================
# LAYER 1: Presentation Layer (TOP)
# ============================================================
layer1_y = 13
layer1_box = FancyBboxPatch((1, layer1_y), 10, 2.2, boxstyle="round,pad=0.15", 
                             edgecolor='#3498db', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(layer1_box)
ax.text(6, layer1_y + 1.9, 'Presentation Layer', ha='center', fontsize=18, fontweight='bold', color='#3498db')

# Components
ax.text(3.5, layer1_y + 1.2, 'Web Interface', ha='center', fontsize=14, fontweight='bold')
ax.text(3.5, layer1_y + 0.8, '(Wartawan)', ha='center', fontsize=12, style='italic')
ax.text(3.5, layer1_y + 0.3, '• Pendaftaran Online', ha='center', fontsize=11)

ax.text(8.5, layer1_y + 1.2, 'Admin Dashboard', ha='center', fontsize=14, fontweight='bold')
ax.text(8.5, layer1_y + 0.8, '(Kominfo)', ha='center', fontsize=12, style='italic')
ax.text(8.5, layer1_y + 0.3, '• Verifikasi & Manajemen', ha='center', fontsize=11)

# ============================================================
# LAYER 2: Application Layer (MIDDLE-TOP)
# ============================================================
layer2_y = 9.5
layer2_box = FancyBboxPatch((1, layer2_y), 10, 2.8, boxstyle="round,pad=0.15", 
                             edgecolor='#27ae60', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(layer2_box)
ax.text(6, layer2_y + 2.5, 'Application Layer', ha='center', fontsize=18, fontweight='bold', color='#27ae60')

# Components
ax.text(3, layer2_y + 1.8, 'Authentication', ha='center', fontsize=13, fontweight='bold')
ax.text(3, layer2_y + 1.4, 'Module', ha='center', fontsize=11)

ax.text(6, layer2_y + 1.8, 'Registration', ha='center', fontsize=13, fontweight='bold')
ax.text(6, layer2_y + 1.4, 'Module', ha='center', fontsize=11)

ax.text(9, layer2_y + 1.8, 'Verification', ha='center', fontsize=13, fontweight='bold')
ax.text(9, layer2_y + 1.4, 'Module', ha='center', fontsize=11)

ax.text(6, layer2_y + 0.7, 'Django Framework (MTV Pattern)', ha='center', fontsize=12, 
        style='italic', color='#27ae60')
ax.text(6, layer2_y + 0.2, 'Models • Templates • Views', ha='center', fontsize=11)

# ============================================================
# LAYER 3: Data Layer (MIDDLE-BOTTOM)
# ============================================================
layer3_y = 7.5
layer3_box = FancyBboxPatch((1, layer3_y), 10, 1.5, boxstyle="round,pad=0.15", 
                             edgecolor='#e74c3c', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(layer3_box)
ax.text(6, layer3_y + 1.1, 'Data Layer', ha='center', fontsize=18, fontweight='bold', color='#e74c3c')
ax.text(6, layer3_y + 0.5, 'PostgreSQL Database', ha='center', fontsize=14, fontweight='bold')

# ============================================================
# LAYER 4: Security Layer (MIDDLE)
# ============================================================
layer4_y = 5
layer4_box = FancyBboxPatch((1, layer4_y), 10, 2, boxstyle="round,pad=0.15", 
                             edgecolor='#f39c12', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(layer4_box)
ax.text(6, layer4_y + 1.6, 'Security Layer', ha='center', fontsize=18, fontweight='bold', color='#f39c12')

# Components
ax.text(3, layer4_y + 0.9, 'Input Validation', ha='center', fontsize=13, fontweight='bold')
ax.text(6, layer4_y + 0.9, 'CSRF Protection', ha='center', fontsize=13, fontweight='bold')
ax.text(9, layer4_y + 0.9, 'Session Management', ha='center', fontsize=13, fontweight='bold')

ax.text(6, layer4_y + 0.3, 'Django Security Features', ha='center', fontsize=11, style='italic')

# ============================================================
# LAYER 5: Infrastructure (BOTTOM)
# ============================================================
layer5_y = 2.5
layer5_box = FancyBboxPatch((1, layer5_y), 10, 1.8, boxstyle="round,pad=0.15", 
                             edgecolor='#34495e', facecolor='#ecf0f1', linewidth=3)
ax.add_patch(layer5_box)
ax.text(6, layer5_y + 1.4, 'Infrastructure', ha='center', fontsize=18, fontweight='bold', color='#34495e')

# Components
ax.text(4, layer5_y + 0.7, 'Nginx', ha='center', fontsize=14, fontweight='bold')
ax.text(4, layer5_y + 0.3, 'Web Server', ha='center', fontsize=11)

ax.text(8, layer5_y + 0.7, 'Gunicorn', ha='center', fontsize=14, fontweight='bold')
ax.text(8, layer5_y + 0.3, 'WSGI Server', ha='center', fontsize=11)

# ============================================================
# EXTERNAL SERVICES (RIGHT SIDE)
# ============================================================
ext_y = 11
ext_box = FancyBboxPatch((11.2, ext_y), 0, 0, boxstyle="round,pad=0", 
                          edgecolor='none', facecolor='none', linewidth=0)

# Email Service
email_box = FancyBboxPatch((0.3, ext_y + 1.5), 0, 0, boxstyle="round,pad=0", 
                            edgecolor='#9b59b6', facecolor='#f3e5f5', linewidth=2.5)
ax.text(0.3, ext_y + 2, 'Email', ha='left', fontsize=13, fontweight='bold', color='#9b59b6')
ax.text(0.3, ext_y + 1.6, 'Notification', ha='left', fontsize=11, color='#9b59b6')

# File Storage
file_box = FancyBboxPatch((0.3, ext_y), 0, 0, boxstyle="round,pad=0", 
                           edgecolor='#9b59b6', facecolor='#f3e5f5', linewidth=2.5)
ax.text(0.3, ext_y + 0.5, 'File Storage', ha='left', fontsize=13, fontweight='bold', color='#9b59b6')
ax.text(0.3, ext_y + 0.1, '(Documents)', ha='left', fontsize=11, color='#9b59b6')

# ============================================================
# ARROWS - Vertical Flow
# ============================================================

# Layer 1 -> Layer 2
arrow1 = FancyArrowPatch((6, layer1_y), (6, layer2_y + 2.8),
                         arrowstyle='->', mutation_scale=30, linewidth=3, color='#34495e')
ax.add_patch(arrow1)
ax.text(6.5, (layer1_y + layer2_y + 2.8)/2, 'HTTP Request', fontsize=11, style='italic', color='#34495e')

# Layer 2 -> Layer 3
arrow2 = FancyArrowPatch((6, layer2_y), (6, layer3_y + 1.5),
                         arrowstyle='->', mutation_scale=30, linewidth=3, color='#34495e')
ax.add_patch(arrow2)
ax.text(6.5, (layer2_y + layer3_y + 1.5)/2, 'ORM Query', fontsize=11, style='italic', color='#34495e')

# Layer 3 -> Layer 2 (Response)
arrow3 = FancyArrowPatch((5.5, layer3_y + 1.5), (5.5, layer2_y),
                         arrowstyle='->', mutation_scale=30, linewidth=3, color='#e74c3c', linestyle='--')
ax.add_patch(arrow3)
ax.text(4.8, (layer2_y + layer3_y + 1.5)/2, 'Data', fontsize=11, style='italic', color='#e74c3c')

# Layer 2 -> Layer 1 (Response)
arrow4 = FancyArrowPatch((5.5, layer2_y + 2.8), (5.5, layer1_y),
                         arrowstyle='->', mutation_scale=30, linewidth=3, color='#27ae60', linestyle='--')
ax.add_patch(arrow4)
ax.text(4.8, (layer1_y + layer2_y + 2.8)/2, 'Response', fontsize=11, style='italic', color='#27ae60')

# External Services -> Layer 2
arrow5 = FancyArrowPatch((1, ext_y + 1.8), (2, layer2_y + 2),
                         arrowstyle='<->', mutation_scale=25, linewidth=2.5, color='#9b59b6', linestyle=':')
ax.add_patch(arrow5)

# Data Flow Indicator (Bottom)
ax.text(6, 1.5, 'Data Flow: User Request → Presentation → Application → Data', 
        ha='center', fontsize=11, style='italic', color='#7f8c8d')
ax.text(6, 1.0, 'Security & Validation Applied at Each Layer', 
        ha='center', fontsize=11, style='italic', color='#e74c3c')

plt.tight_layout()
plt.savefig('architecture_diagram.jpg', dpi=400, bbox_inches='tight', pad_inches=0.2)
print("[OK] PORTRAIT Architecture Diagram saved!")
plt.close()

print("\n" + "="*60)
print("[OK] CLEAN ARCHITECTURE DIAGRAM GENERATED!")
print("="*60)
print("\nFeatures:")
print("- PORTRAIT orientation (12×16)")
print("- NO title at top")
print("- NO legend at bottom")
print("- LARGER components and text")
print("- 5 layers clearly defined")
print("- Vertical data flow with arrows")
print("- Clean, professional design")
