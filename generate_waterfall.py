import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Polygon
import numpy as np

# Set style
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 13

print("Generating PORTRAIT Waterfall Diagram (Clean)...")

# PORTRAIT: taller than wide
fig, ax = plt.subplots(figsize=(12, 16))
ax.set_xlim(0, 12)
ax.set_ylim(0, 16)
ax.axis('off')

# ============================================================
# Waterfall Phases (5 phases cascading down)
# ============================================================

phases = [
    {
        'name': 'Requirements Analysis',
        'name_id': 'Analisis Kebutuhan',
        'y': 13,
        'color': '#3498db',
        'description': '• Identifikasi kebutuhan sistem\n• Analisis proses bisnis\n• Dokumentasi requirements'
    },
    {
        'name': 'System Design',
        'name_id': 'Perancangan Sistem',
        'y': 10,
        'color': '#27ae60',
        'description': '• Desain arsitektur sistem\n• Desain database (ERD)\n• Desain UML (Use Case, Activity)'
    },
    {
        'name': 'Implementation',
        'name_id': 'Implementasi',
        'y': 7,
        'color': '#f39c12',
        'description': '• Coding dengan Django\n• Integrasi komponen\n• Unit testing'
    },
    {
        'name': 'Testing',
        'name_id': 'Pengujian',
        'y': 4,
        'color': '#e74c3c',
        'description': '• Black box testing\n• System testing\n• User acceptance testing'
    },
    {
        'name': 'Deployment',
        'name_id': 'Deployment',
        'y': 1,
        'color': '#9b59b6',
        'description': '• Instalasi sistem\n• Pelatihan pengguna\n• Maintenance'
    }
]

# Draw each phase
for i, phase in enumerate(phases):
    y = phase['y']
    x_offset = i * 0.8  # Cascade effect
    
    # Main box
    box = FancyBboxPatch((1 + x_offset, y), 8, 2.2, 
                          boxstyle="round,pad=0.1", 
                          edgecolor=phase['color'], 
                          facecolor='#ecf0f1', 
                          linewidth=3.5)
    ax.add_patch(box)
    
    # Header bar
    header = Rectangle((1 + x_offset, y + 1.5), 8, 0.7,
                       facecolor=phase['color'], 
                       edgecolor=phase['color'], 
                       linewidth=0)
    ax.add_patch(header)
    
    # Phase name (English)
    ax.text(5 + x_offset, y + 1.85, phase['name'], 
            ha='center', va='center', 
            fontsize=15, fontweight='bold', color='white')
    
    # Phase name (Indonesian)
    ax.text(5 + x_offset, y + 1.2, phase['name_id'], 
            ha='center', va='center', 
            fontsize=13, style='italic', color=phase['color'])
    
    # Description
    ax.text(5 + x_offset, y + 0.5, phase['description'], 
            ha='center', va='center', 
            fontsize=11, color='#2c3e50')
    
    # Arrow to next phase (if not last)
    if i < len(phases) - 1:
        next_y = phases[i+1]['y']
        next_x_offset = (i+1) * 0.8
        
        # Curved arrow
        arrow = FancyArrowPatch(
            (5 + x_offset, y),
            (5 + next_x_offset, next_y + 2.2),
            arrowstyle='->', 
            mutation_scale=40, 
            linewidth=4, 
            color='#34495e',
            connectionstyle="arc3,rad=0.3"
        )
        ax.add_patch(arrow)
        
        # Phase number
        ax.text(5 + x_offset - 1.5, y + 1.1, f'{i+1}', 
                ha='center', va='center',
                fontsize=20, fontweight='bold', 
                color=phase['color'],
                bbox=dict(boxstyle='circle,pad=0.3', 
                         facecolor='white', 
                         edgecolor=phase['color'], 
                         linewidth=3))

# Last phase number
ax.text(5 + 4*0.8 - 1.5, 2.1, '5', 
        ha='center', va='center',
        fontsize=20, fontweight='bold', 
        color=phases[4]['color'],
        bbox=dict(boxstyle='circle,pad=0.3', 
                 facecolor='white', 
                 edgecolor=phases[4]['color'], 
                 linewidth=3))

# ============================================================
# Feedback arrows (dotted - showing iterative nature)
# ============================================================

# Testing -> Implementation (if bugs found)
feedback1 = FancyArrowPatch(
    (1.5 + 3*0.8, 4.5),
    (1.5 + 2*0.8, 7.5),
    arrowstyle='<-', 
    mutation_scale=25, 
    linewidth=2, 
    color='#95a5a6',
    linestyle='--',
    alpha=0.6
)
ax.add_patch(feedback1)
ax.text(0.8, 6, 'Bug Fix', fontsize=10, style='italic', color='#7f8c8d', rotation=60)

# Implementation -> Design (if design issues)
feedback2 = FancyArrowPatch(
    (1.5 + 2*0.8, 7.5),
    (1.5 + 1*0.8, 10.5),
    arrowstyle='<-', 
    mutation_scale=25, 
    linewidth=2, 
    color='#95a5a6',
    linestyle='--',
    alpha=0.6
)
ax.add_patch(feedback2)
ax.text(0.8, 9, 'Revisi', fontsize=10, style='italic', color='#7f8c8d', rotation=60)

plt.tight_layout()
plt.savefig('waterfall.jpg', dpi=400, bbox_inches='tight', pad_inches=0.2)
print("[OK] PORTRAIT Waterfall Diagram saved!")
plt.close()

print("\n" + "="*60)
print("[OK] CLEAN WATERFALL DIAGRAM GENERATED!")
print("="*60)
print("\nFeatures:")
print("- PORTRAIT orientation (12×16)")
print("- NO title at top")
print("- NO legend at bottom")
print("- 5 phases with cascade effect")
print("- Clear phase descriptions")
print("- Forward arrows (main flow)")
print("- Feedback arrows (iteration)")
print("- Bilingual labels (EN + ID)")
print("- Clean, professional design")
