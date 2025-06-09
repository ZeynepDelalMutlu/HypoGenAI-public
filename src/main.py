import pdfplumber
import os

INPUT_DIR = "data/docs"
OUTPUT_DIR = "data/txt"

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n\n--- Page {page_num + 1} ---\n\n"
                text += page_text
    return text

def process_all_pdfs(input_dir, output_dir):
    if not os.path.exists(input_dir):
        print(f"Input directory not found: {input_dir}")
        return

    os.makedirs(output_dir, exist_ok=True)

    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in the input directory.")
        return

    for file_name in pdf_files:
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name.replace(".pdf", ".txt"))

        print(f"Processing: {file_name}")
        try:
            extracted_text = extract_text_from_pdf(input_path)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(extracted_text)
            print(f"Saved to: {output_path}")
        except Exception as e:
            print(f"Failed to process {file_name}: {e}")

if __name__ == "__main__":
    process_all_pdfs(INPUT_DIR, OUTPUT_DIR)
