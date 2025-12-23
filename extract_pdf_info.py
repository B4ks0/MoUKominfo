import os
import re

# Try to extract basic info from PDF filenames and attempt simple text extraction
references_dir = r"C:\laragon\www\MoUKominfo\references"

pdf_files = [
    "2.+PENGEMBANGAN+APLIKASI+PENILAIAN+OUTCOME-BASED+EDUCATION+(OBE)+BERBASIS+WEBSITE+DENGAN+METODE+WATERFALL.pdf",
    "4.+RANCANG+BANGUN+SISTEM+INFORMASI+PENJUALAN+DAN+PIUTANG+BERBASIS+WEBSITE+PADA+TOKO+INTI+ALAM.pdf",
    "18-Article Text-33-2-10-20201228.pdf",
    "19-Article Text-35-2-10-20201228.pdf",
    "125-Article Text-524-1-10-20230630.pdf",
    "158-Article Text-947-4-10-20250630.pdf",
    "197-Article Text-522-1-10-20230630.pdf",
    "241-Article Text-674-1-10-20231221.pdf",
    "90898+Completed+50-62+-+Copy.pdf",
    "Rancang+Bangun+Sistem+Informasi+E-commerce+Berbasis+Website+(Studi+Kasus+Toko+Komputer+di+Denpasar).pdf"
]

print("PDF Files Found:")
print("=" * 80)
for i, pdf in enumerate(pdf_files, 1):
    # Decode URL encoding
    decoded = pdf.replace('+', ' ')
    print(f"\n{i}. {decoded}")
    
    # Try to extract year from filename
    year_match = re.search(r'(\d{4})', pdf)
    if year_match:
        print(f"   Possible Year: {year_match.group(1)}")
    
    # Get file size
    filepath = os.path.join(references_dir, pdf)
    if os.path.exists(filepath):
        size_kb = os.path.getsize(filepath) / 1024
        print(f"   Size: {size_kb:.1f} KB")

print("\n" + "=" * 80)
print("\nAttempting to read PDF metadata using PyPDF2...")

try:
    import PyPDF2
    
    for pdf in pdf_files[:3]:  # Try first 3 files
        filepath = os.path.join(references_dir, pdf)
        try:
            with open(filepath, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                info = reader.metadata
                
                print(f"\n\nFile: {pdf.replace('+', ' ')}")
                print("-" * 60)
                if info:
                    for key, value in info.items():
                        print(f"{key}: {value}")
                
                # Try to extract first page text
                if len(reader.pages) > 0:
                    first_page = reader.pages[0].extract_text()
                    # Get first 500 characters
                    print("\nFirst page excerpt:")
                    print(first_page[:500])
        except Exception as e:
            print(f"Error reading {pdf}: {e}")
            
except ImportError:
    print("PyPDF2 not installed. Install with: pip install PyPDF2")
