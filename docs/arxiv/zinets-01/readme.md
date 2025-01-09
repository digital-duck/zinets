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

python md2tex2pdf.py

