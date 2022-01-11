import os
import glob
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


if __name__ == "__main__":
    print(find_pdfs('../../data/external'))
