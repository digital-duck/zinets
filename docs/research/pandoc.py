import pypandoc

file_pdf = "zinets-v0.5.pdf"
file_md = "zinets-v0.5.md"

# Basic test
pypandoc.convert_file(
    file_md, 
    'pdf', 
    outputfile=file_pdf,
    extra_args=[
        '--pdf-engine=xelatex',
        '-V', 'CJKmainfont=SimSun'  # For Chinese text
    ]
)
