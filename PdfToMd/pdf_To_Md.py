import pdfplumber
from markdownify import markdownify


def convert_pdf_to_md(pdf_path, md_path):
    # Step 1: Extract text from PDF
    text_content = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text_content += page.extract_text() + "\n\n"

    # Step 2: Convert text to Markdown
    markdown_content = markdownify(text_content)

    # Step 3: Write Markdown to a file
    with open(md_path, "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

    print(f"Markdown file created at {md_path}")


# Input and output file paths
pdf_file_path = (
    "/home/mss/Desktop/ProblemSolving/Python/PdfToMd/Commands/LinuxBasicCommands.pdf"
)
markdown_file_path = (
    "/home/mss/Desktop/ProblemSolving/Python/PdfToMd/LinuxBasicCommands.md"
)

convert_pdf_to_md(pdf_file_path, markdown_file_path)
