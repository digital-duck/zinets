```bash
pandoc --version
xelatex --version
fc-list :lang=zh

pandoc ustc-journal-ENU-v0.5.md -o ustcj2025-2.tex --pdf-engine=xelatex
pandoc ustc-journal-ENU-v0.5.md -o ustcj2025-2.pdf --pdf-engine=xelatex

# pandoc zinets-v0.8.md -o zinets.tex --pdf-engine=xelatex
# pandoc zinets-v0.8.md -o zinets.pdf --pdf-engine=xelatex


python3 pandoc-md2pdf.py
python3 pandoc-tex2pdf.py
python3 pandoc-md2latex.py


python3 md2tex2pdf.py

python3 prepare_arxiv.py
```

https://claude.ai/chat/e3c34389-5dcb-4971-a88c-9512c2d9db9b


conda activate zinets
sudo apt update
sudo apt install pandoc

pandoc --version  # pandoc 3.2

pip install pypandoc

sudo apt install texlive-xetex texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra

pip install Pillow  # For image handling

# Install Chinese/CJK support packages for XeLaTeX
sudo apt install texlive-lang-chinese
sudo apt install latex-cjk-all
sudo apt install texlive-full


sudo texhash
sudo mktexlsr


### Final manual editing for submission of zinets-v0.9.md
```
python md2tex2pdf.py
python prepare_arxiv-v1.py
cp -rf zinets-v0.9_arxiv zinets_arxiv
```

ToDo:
- line breaking

line 624

- resize image

- edit figure caption

\usepackage{xeCJK}
\setCJKmainfont{Noto Sans CJK SC}

```
sudo apt-get update
sudo apt-get install texlive-xetex
sudo apt-get install texlive-lang-chinese
sudo apt-get install fonts-noto-cjk

xelatex zinets.tex

zip -r zinets_arxiv.zip zinets_arxiv

```


Failed to submit at arxiv.org
due to PDFLATEX
submit/6121470

contacted Tech Support at arxiv.org

Your reference is AH-125704.