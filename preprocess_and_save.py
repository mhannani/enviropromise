import os.path
from tqdm import tqdm
from src.config import *
from src.utils.jsonify import clean_jsonify_save
from src.utils.find import find_pdfs
from src.utils.save import save_to_text
from src.utils.preprocess import pdf_to_text


def preprocess_and_save_pdfs(directory: str, txt_out: str = TXT_OUT, json_out: str = JSON_OUT) -> None:
    """
    Preprocesses, cleans and save all PDFs contents to files with the same filenames.
    :param directory: str
        Path to directory of data.
    :param txt_out: str
        Path where to store/save the text files
    :param json_out: str
        Path where to store/save the json files
    :return: None
    """

    # Get PDFs files
    pdfs = find_pdfs(directory)

    # Preprocess pdfs
    for pdf in tqdm(pdfs, total=len(pdfs), colour='#00ff00', ncols=50):
        # Get pdf content
        text = pdf_to_text(os.path.join(directory, os.path.basename(pdf)))

        filename = os.path.splitext(os.path.basename(pdf))[0]

        # Save pdf to .txt file
        save_to_text(text, filename, txt_out)

        # clean the text to save it to json file
        clean_jsonify_save(text, out=filename)


if __name__ == "__main__":
    preprocess_and_save_pdfs(directory='./data/external/PDFs')
