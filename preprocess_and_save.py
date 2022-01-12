import os.path

from src.utils.find import find_pdfs
from src.utils.save import save_to_text
from src.utils.preprocess import pdf_to_text


def preprocess_and_save_pdfs(directory: str, out: str = './data/interim/') -> None:
    """
    Preprocesses, cleans and save all PDFs contents to files with the same filenames.
    :param directory: str
        Path to directory of data.
    :param out: str
        Path where to store/save the text files
    :return: None
    """

    # Get PDFs files
    pdfs = find_pdfs(directory)

    # Preprocess pdfs
    for pdf in pdfs:
        # Get pdf content
        text = pdf_to_text(os.path.join(directory, os.path.basename(pdf)))

        # Save to file
        filename = os.path.splitext(os.path.basename(pdf))[0]
        save_to_text(text, filename, out)


if __name__ == "__main__":
    preprocess_and_save_pdfs(directory='./data/external/PDFs')
