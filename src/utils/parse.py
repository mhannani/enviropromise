# parser functions
from typing import List, Tuple


def parse_json(path: str) -> Tuple[str, str, int, int, List[str]]:
    """
    Parses the json file and returns a list of sentences/clauses.
    :param path: str
        Path of json files.
    :return: str, str, int, int, List[str]
        filename, date, article number, number of sentences, List of sentences
    """
    pass


if __name__ == "__main__":
    json_path = "../../data/preprocessed/mor96784.json"
    sentences = parse_json(json_path)
    print(sentences[0])
    print('number of sentences:', len(sentences))
