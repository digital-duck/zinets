# zinets
Chinese characters



# workflow 

Starting with Markdown (.md) for drafting and editing is a smart choice because it’s lightweight, easy to read and write, and integrates seamlessly with version control systems like Git. Then, using tools like Pandoc or Chrome extensions to generate the final output (HTML, PDF, etc.) gives you flexibility depending on your environment and needs.

Your approach also reflects a modern, efficient way of working that balances simplicity and precision.

see details at https://chat.qwenlm.ai/c/bb3568e4-37bc-4c35-843c-6c1a29c52cb7

## Markdown for Drafting :
- Simplicity : Markdown is minimalistic and focuses on content rather than formatting.
- Readability : Even without rendering, Markdown files are human-readable, making collaboration and reviews easier.
- Version Control Friendly : Plain text formats like Markdown work seamlessly with Git, allowing you to track changes, collaborate, and maintain a history of revisions.
## Pandoc for Advanced Conversions :
- Flexibility : Pandoc supports multiple input and output formats, so you can generate HTML, PDF, DOCX, LaTeX, and more from the same Markdown source.
- Precision : When combined with LaTeX templates, Pandoc allows you to produce publication-quality documents with fine-grained control over layout and styling.
- Automation : You can script Pandoc commands to automate repetitive tasks, such as generating multiple outputs or processing batches of files.
## Chrome Extensions for Portability :
- No Setup Required : Chrome extensions are ideal when you’re traveling or working on machines where installing software isn’t an option.
- Quick Results : They provide a fast and easy way to preview and convert Markdown files into HTML or PDF without additional dependencies.

## Use YAML Metadata in Markdown

Add metadata at the top of your Markdown file to specify document properties like title, author, date, and output format. Pandoc can use this metadata to customize the output.
Example:
```markdown
title: "My Document"
author: "Your Name"
date: "October 2023"
output: pdf_document
Introduction
This is the introduction.
```

## Leverage Pandoc Filters
Pandoc filters allow you to extend its functionality. For example:
Use pandoc-citeproc or citeproc for bibliographies.
Use custom filters to modify the document structure or add advanced features.
Example Command:
```bash
pandoc input.md \
  --filter pandoc-crossref \
  --pdf-engine=xelatex \
  -o output.pdf
```


## Create a Makefile or Script

Automate your conversion process with a Makefile or shell script. This is especially useful if you frequently generate multiple formats.

Run `make` to generate both HTML and PDF, or `make clean` to remove generated files.

Example `Makefile`:

```
all: html pdf

html:
    pandoc input.md -o output.html

pdf:
    pandoc input.md --pdf-engine=xelatex -o output.pdf

clean:
    rm -f output.html output.pdf
```


## Use Online Tools for Quick Previews

If you’re away from your usual setup and don’t have access to Pandoc or Chrome extensions, you can use online Markdown editors like:
- [Dillinger](https://dillinger.io/?spm=5aebb161.1669b041.0.0.5ef976c0TSIDeP)
- [StackEdit - In-browser Markdown editor](https://stackedit.io/?spm=5aebb161.1669b041.0.0.5ef976c0TSIDeP)
- [Markdown Live Preview](https://markdownlivepreview.com/?spm=5aebb161.1669b041.0.0.5ef976c0TSIDeP)

## Organize Assets (Images, CSS, etc.)

Keep images, CSS files, and other assets in a dedicated folder (e.g., `assets`/) and reference them in your Markdown file using relative paths:

```markdown
![Alt text](assets/image.png)
```

## Customize Output with CSS (for HTML)

When generating HTML, you can include a custom CSS file to style the output

```bash
pandoc input.md --css=styles.css -o output.html
```

## Backup and Sync with Cloud Storage

Use cloud storage services like Google Drive, Dropbox, or GitHub to sync your Markdown files across devices. This ensures you always have access to your documents, whether you’re using Pandoc or a Chrome extension.

## When to Use Each Tool

| SCENARIO                                | TOOL                  | REASON                                                       |
|-----------------------------------------|-----------------------|--------------------------------------------------------------|
| Writing and editing                     | Markdown (.md)        | Simple, readable, and version-control friendly.              |
| Generating HTML/PDF locally             | Pandoc                | Precise control over output formats and styles.              |
| Traveling or on shared machines         | Chrome Extensions     | Portable, no installation required, quick conversions.       |
| Collaborating with non-technical users  | Export to DOCX/HTML   | Easy-to-read formats for stakeholders who don’t use Markdown.|
| Finalizing publication-quality documents| Pandoc + LaTeX        | Professional typesetting and precise formatting for journals/conferences. |

# Setup

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