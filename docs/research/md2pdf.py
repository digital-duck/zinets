from markdown_pdf import MarkdownPdf

# Create instance
md_pdf = MarkdownPdf()

file_pdf = "zinets-v0.5.pdf"
file_md = "zinets-v0.5.md"
md_pdf.convert(file_md, file_pdf)

"""
import markdown
import pdfkit

file_pdf = "zinets-v0.5.pdf"
file_md = "zinets-v0.5.md"

# First convert MD to HTML
html = markdown.markdown(open(file_md, encoding="utf-8").read())

# Then HTML to PDF
pdfkit.from_string(html, file_pdf)
"""
