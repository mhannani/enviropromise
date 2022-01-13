# parser functions
import json
from typing import List, Tuple


def parse_json(path: str) -> Tuple[str, str, int, int, List[str]]:
    """
    Parses the json file and returns a list of sentences/clauses.
    :param path: str
        Path of json files.
    :return: str, str, int, int, List[str]
        filename, date, article number, number of sentences, List of sentences
    """
    # read json file
    with open(path, 'r') as json_file:
        content = json.load(json_file)

    # get entities
    filename = content['filename']
    date = content['date']
    n_article = content['article number']
    sentences_len = content['len']
    sentences = content['sentences']

    return filename, date, n_article, sentences_len, sentences


if __name__ == "__main__":
    json_path = "../../data/preprocessed/mor96784.json"
    file_name, d, n_art, sen_len, sens = parse_json(json_path)
    print('filename:', file_name)
    print('date:', d)
    print('len:', sen_len)
