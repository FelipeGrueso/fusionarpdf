from PyPDF2 import PdfReader, PdfWriter
import os

def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()
    if len(paths) != 0:
        for path in paths:
            pdf_reader = PdfReader(path)
            for page in pdf_reader.pages:  # Corrected the range function
                # Add each page to the writer object
                pdf_writer.add_page(page)  # Corrected the method name

        # Write out the merged PDF
        with open(output, 'wb') as out:
            pdf_writer.write(out)

if __name__ == '__main__':
    pdfs = [archivo for archivo in os.listdir('./') if archivo.endswith(".pdf")]
    pdfs.sort(reverse=False)
    salida = pdfs[0][0:-4] + "-fusionado.pdf"

    merge_pdfs(pdfs, output=salida)


###pyinstaller --windowed --onefile --icon=./icono-PDF.ico PDFUT4Gv2.py
