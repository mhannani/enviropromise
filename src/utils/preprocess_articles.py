from io import StringIO
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.pdfpage import PDFPage


def pdf_to_text(pdf: str, use_high_level=False) -> str:
    """
    Converts PDFS files to text.
    An adapted version of: https://github.com/pdfminer/pdfminer.six/blob/develop/pdfminer/high_level.py
    from official pdfminer project repository.
    :param pdf: str
        File path to the PDF file.
    :param use_high_level: boolean, default False
        Whether to use the high level API to extract text from pdf
        default False, use low level if True.

    :return: str
        Text-based content of the input PDF.
    """

    if use_high_level:
        from pdfminer.high_level import extract_text
        text = extract_text(pdf)
        return text

    output_string = StringIO()

    # read the PDF file
    with open(pdf, 'rb') as in_file:
        # Fetch PDF objects from a file stream.
        parser = PDFParser(in_file)

        # Dynamically import the data as processing goes and prevents loading
        # the entire pdf as it can be very big.
        doc = PDFDocument(parser)

        # facilitate reuse of shared resources such image and fonts
        rsrcmgr = PDFResourceManager()

        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

        # get the content as text
        text = output_string.getvalue()
        device.close()
        output_string.close()

    return text


if __name__ == "__main__":
    path = '../../paper/paper.pdf'
    print(pdf_to_text(path))

