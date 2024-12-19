import os
import pdfplumber
from markdownify import markdownify


def convert_pdf_to_md(pdf_path, md_path):
    # Extract text from PDF
    text_content = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text_content += page.extract_text() + "\n\n"

    # Convert text to Markdown
    markdown_content = markdownify(text_content)

    # Save to .md file
    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    print(f"Markdown file created: {md_path}")


def convert_multiple_pdfs(pdf_dir, md_dir):
    # Ensure the output directory exists
    os.makedirs(md_dir, exist_ok=True)

    # Loop through all PDF files in the input directory
    for file_name in os.listdir(pdf_dir):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(pdf_dir, file_name)
            md_path = os.path.join(md_dir, file_name.replace(".pdf", ".md"))

            # Convert PDF to Markdown
            convert_pdf_to_md(pdf_path, md_path)


# Input and output directories
pdf_directory = "/home/mss/Desktop/ProblemSolving/Python/PdfToMd/Commands/"
md_directory = "/home/mss/Desktop/ProblemSolving/Python/PdfToMd/MarkdownFiles"

convert_multiple_pdfs(pdf_directory, md_directory)
