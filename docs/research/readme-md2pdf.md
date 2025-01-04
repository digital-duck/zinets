Here are the detailed installation steps:

Install Pandoc system package:

Windows: Download installer from https://pandoc.org/installing.html
Or use Chocolatey: choco install pandoc
Verify installation: pandoc --version


Install LaTeX distribution:

For Windows, MiKTeX is recommended: https://miktex.org/download
During MiKTeX installation:

Choose "Install missing packages on the fly = Yes"
This will auto-download CJK packages when needed


Verify installation: pdflatex --version


Install pypandoc:

pip install pypandoc
cd C:\Users\p2p2l\projects\digital-duck\zinets\docs\research


import pypandoc

# Basic test
pypandoc.convert_file(
    'input.md', 
    'pdf', 
    outputfile='output.pdf',
    extra_args=[
        '--pdf-engine=xelatex',
        '-V', 'CJKmainfont=SimSun'  # For Chinese text
    ]
)

