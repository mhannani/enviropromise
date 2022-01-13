import os
from typing import List


def find_pdfs(directory: str) -> List[str]:
    """
    Recursively finds all PDFs file in `directory`.
    :param directory: str
        Directory's absolute path
    :return: List of path of PDFs found in `directory`.
    """

    # list of PDFs files
    pdfs = []

    for root, folders, files in os.walk(directory):
        for file in files:
            if file.endswith('pdf'):
                pdfs.append(file)

    return pdfs


def find_json(directory: str) -> List[str]:
    """
    Recursively finds json files and returns list of found paths.

    :param directory: str
        Path to directory where json files resides
    :return: List[str]
        List of absolute paths
    """

    jsons = []
    for root, folders, files in os.walk(directory):
        for file in files:
            if file.endswith('json'):
                jsons.append(file)

    return jsons


if __name__ == "__main__":
    # print(find_pdfs('../../data/external'))
    print(find_json('../../data/preprocessed'))
