```bash
pandoc --version
xelatex --version
fc-list :lang=zh

pandoc zinets-v0.8.md -o zinets.tex --pdf-engine=xelatex
pandoc zinets-v0.8.md -o zinets.pdf --pdf-engine=xelatex


python3 pandoc-md2pdf.py
python3 pandoc-tex2pdf.py
python3 pandoc-md2latex.py


python3 md2tex2pdf.py

python3 prepare_arxiv.py
```