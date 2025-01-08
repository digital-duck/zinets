import pypandoc
import subprocess

file_name = "zinets-v0.8"
file_tex = f"{file_name}.tex"
file_md = f"{file_name}.md"
file_pdf = f"{file_name}.pdf"

# First convert MD to TEX
pypandoc.convert_file(
    file_md, 
    'latex', 
    outputfile=file_tex,
    extra_args=[
        '--pdf-engine=xelatex',
        '--standalone',
        '-V', 'documentclass=article',
        '-V', 'CJKmainfont=Noto Sans CJK TC Medium',
        '-V', 'geometry=margin=0.75in',
        '-V', 'fontsize=11pt',
        '-V', 'papersize=letter'
    ]
)

# Then compile TEX to PDF using xelatex
try:
    subprocess.run(['xelatex', file_tex], check=True)
    # Run twice for references and TOC if needed
    subprocess.run(['xelatex', file_tex], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error converting to PDF: {e}")