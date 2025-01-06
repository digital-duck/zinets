import pypandoc

file_name = "zinets-v0.8-cn" # "zinets-v0.8" # "zinets-v0.5"
file_pdf = f"{file_name}.pdf"
file_md = f"{file_name}.md"

# Basic test
pypandoc.convert_file(
    file_md, 
    'pdf', 
    outputfile=file_pdf,
    extra_args=[
        '--pdf-engine=xelatex',
        '-V', 'CJKmainfont=SimSun',  # For Chinese text
        '-V', 'geometry=margin=0.75in',  # adjust margins
        '-V', 'fontsize=11pt',        # change font size
        '-V', 'papersize=letter',         # set paper size        
    ]
)
