import PyPDF2
import os
import re

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

references = []

for i, pdf in enumerate(pdf_files, 1):
    filepath = os.path.join(references_dir, pdf)
    try:
        with open(filepath, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            
            # Get first page text
            if len(reader.pages) > 0:
                first_page = reader.pages[0].extract_text()
                
                # Extract author, title, journal, year, volume, pages
                ref_info = {
                    'num': i,
                    'filename': pdf.replace('+', ' '),
                    'text': first_page[:1500]  # First 1500 chars
                }
                
                references.append(ref_info)
                
    except Exception as e:
        print(f"Error reading {pdf}: {e}")

# Print formatted output
print("EXTRACTED REFERENCES:")
print("=" * 100)

for ref in references:
    print(f"\n[{ref['num']}] File: {ref['filename']}")
    print("-" * 100)
    print(ref['text'])
    print("\n")

# Try to format as LaTeX bibliography
print("\n\n")
print("SUGGESTED LATEX BIBLIOGRAPHY FORMAT:")
print("=" * 100)

for ref in references:
    text = ref['text']
    
    # Try to extract author names (usually at the beginning or after title)
    # Try to extract journal name
    # Try to extract year, volume, pages
    
    # Look for common patterns
    author_match = re.search(r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)', text)
    year_match = re.search(r'(20\d{2})', text)
    vol_match = re.search(r'[Vv]ol\.?\s*(\d+)', text)
    no_match = re.search(r'[Nn]o\.?\s*(\d+)', text)
    pages_match = re.search(r'(?:pp?\.?\s*)?(\d+)\s*[-–]\s*(\d+)', text)
    
    author = author_match.group(1) if author_match else "Author Name"
    year = year_match.group(1) if year_match else "Year"
    vol = vol_match.group(1) if vol_match else "X"
    no = no_match.group(1) if no_match else "X"
    pages = f"{pages_match.group(1)}-{pages_match.group(2)}" if pages_match else "XX-XX"
    
    # Extract title (usually in caps or after author)
    title_lines = text.split('\n')[:10]
    title = "Article Title"
    for line in title_lines:
        if len(line) > 20 and line.isupper() and 'ISSN' not in line:
            title = line.strip()
            break
    
    print(f"\n[{ref['num']}] {author}, \"{title},\" \\textit{{Journal Name}}, vol. {vol}, no. {no}, pp. {pages}, {year}.")

