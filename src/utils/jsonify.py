import os
from src.config import *
import json
from .clean import clean_txt


def clean_jsonify_save(filename: str, out: str):
    """
    Clean and jsonify the text in the given file.
    :return: None
    """

    # clean text
    sentences, _, date, n_article = clean_txt(filename)

    # jsonify data
    data = {
            'filename': out,
            'date': date,
            'article number': n_article,
            'len': len(sentences),
            'sentences': sentences
        }

    # dump json data to file
    with open(os.path.join(JSON_OUT, f'{out}.json'), 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    file_name = '../../data/interim/Mor106711.txt'
    clean_jsonify_save(file_name, out='../../data/preprocessed')
