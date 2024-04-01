

import re
import os
from datetime import datetime
from PyPDF2 import PdfFileReader, PdfFileWriter

# Define input and output directories
pdf_data_dir = "pdf_data"
outfile_dir = datetime.now().strftime("%Y-%m-%d")

# Create the output directory if it doesn't exist
if not os.path.exists(outfile_dir):
    os.mkdir(outfile_dir)

xpress_bees_output_pdf = PdfFileWriter()
ecom_express_output_pdf = PdfFileWriter()
Delhivery_output_pdf = PdfFileWriter()
Shadowfax_output_pdf = PdfFileWriter()
Valmo_output_pdf = PdfFileWriter()

# List PDF files in the pdf_data directory
pdfs = [file for file in os.listdir(pdf_data_dir) if file.endswith(".pdf")]

for pdf_single in pdfs:
    pdf_file_path = os.path.join(pdf_data_dir, pdf_single)

    reader = PdfFileReader(pdf_file_path)
    number_of_pages = reader.getNumPages()

    for page_num in range(number_of_pages):
        page = reader.getPage(page_num)
        text = page.extractText()

        match = re.search(r"Xpress Bees|Ecom Express|Delhivery|Shadowfax|Valmo", text, re.IGNORECASE)

        if match:
            current_partner = match.group()
            if current_partner == "Xpress Bees":
                xpress_bees_output_pdf.addPage(page)
            elif current_partner == "Ecom Express":
                ecom_express_output_pdf.addPage(page)
            elif current_partner == "Delhivery":
                Delhivery_output_pdf.addPage(page)
            elif current_partner == "Shadowfax":
                Shadowfax_output_pdf.addPage(page)
            elif current_partner == "Valmo":
                Valmo_output_pdf.addPage(page)

if xpress_bees_output_pdf.getNumPages() > 0:
    with open(os.path.join(outfile_dir, "Xpress Bees.pdf"), "wb") as xpress_bees_output_pdfoutput_file:
        xpress_bees_output_pdf.write(xpress_bees_output_pdfoutput_file)

if ecom_express_output_pdf.getNumPages() > 0:
    with open(os.path.join(outfile_dir, "Ecom Express.pdf"), "wb") as ecom_express_output_pdfoutput_file:
        ecom_express_output_pdf.write(ecom_express_output_pdfoutput_file)

if Delhivery_output_pdf.getNumPages() > 0:
    with open(os.path.join(outfile_dir, "Delhivery.pdf"), "wb") as Delhivery_output_pdfoutput_file:
        Delhivery_output_pdf.write(Delhivery_output_pdfoutput_file)

if Shadowfax_output_pdf.getNumPages() > 0:
    with open(os.path.join(outfile_dir, "Shadowfax.pdf"), "wb") as Shadowfax_output_pdfoutput_file:
        Shadowfax_output_pdf.write(Shadowfax_output_pdfoutput_file)

if Valmo_output_pdf.getNumPages() > 0:
    with open(os.path.join(outfile_dir, "Valmo.pdf"), "wb") as Valmo_output_pdfoutput_file:
        Valmo_output_pdf.write(Valmo_output_pdfoutput_file)
