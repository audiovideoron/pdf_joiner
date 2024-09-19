import PyPDF2
import argparse


def merge_pdfs(pdf_list, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        with open(pdf, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            # Decrypt if the PDF is encrypted (assuming you know the password)
            if reader.is_encrypted:
                try:
                    reader.decrypt('')
                    print(f"{pdf} was decrypted successfully.")
                except Exception as e:
                    print(f"Could not decrypt {pdf}: {e}")
                    continue  # Skip this file if it can't be decrypted

            pdf_merger.append(reader)

    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Merge multiple PDF files into a single file.")

    # Positional arguments for input PDF files and output file
    parser.add_argument('pdf_files', nargs='+', help="List of PDF files to merge")
    parser.add_argument('-o', '--output', required=True, help="Output filename for the merged PDF")

    # Parse arguments
    args = parser.parse_args()

    # Merge the PDFs
    merge_pdfs(args.pdf_files, args.output)
    print(f'Merged PDF saved as {args.output}')
