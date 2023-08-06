from PyPDF2 import PdfFileWriter, PdfFileReader


def pdfspliter(pdf, newname):

    '''
    Splits the given pdf
    :param pdf:
    :param newname:
    :return:
    '''

    pdf_r = PdfFileReader(pdf)

    for page in range(pdf_r.getNumPages()):
        pdf_w = PdfFileWriter()
        pdf_w.addPage(pdf_r.getPage(page))

        out_name = f'{newname}_{page + 1}.pdf'

        with open(out_name, 'wb') as out:
            pdf_w.write(out)


def pdfmerger(pdf1, pdf2, dstpdf):

    '''
    Merge the given two PDFs in another one
    :param pdf1:
    :param pdf2:
    :param dstpdf:
    :return:
    '''

    pdf_li = [PdfFileReader(pdf1), PdfFileReader(pdf2)]
    pdf_w = PdfFileWriter()

    for p in pdf_li:
        for page in range(p.getNumPages()):
            pdf_w.addPage(p.getPage(page))

    with open(dstpdf, 'wb') as out:
        pdf_w.write(out)
