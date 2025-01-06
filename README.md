# zinets
Chinese characters



# md2pdf

```
conda activate zinet
cd digital-duck\zinets\docs\research

pip install md2pdf

from md2pdf.core import md2pdf

file_pdf = "zinets-v0.5.pdf"
file_md = "analyzing-chinese-characters-via-physics-lens-v0.5.md"
md2pdf(file_pdf, file_md)

```

cd digital-duck\zinets\docs\overleaf\zinets-01

\usepackage[UTF8]{ctex}

pandoc -s zinets-v0.8.md -o zinets-v0.8.tex

https://chat.deepseek.com/a/chat/s/6fec3b04-a747-4e50-9d07-c0646073a22e


In Overleaf, click the Menu button (top-left corner).

Under Settings, change the Compiler to XeLaTeX