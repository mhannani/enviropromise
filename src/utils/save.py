from typing import List
import csv
import os.path


def save_to_text(text: str, filename: str, out: str) -> None:
    """
    Saves the content of PDF file to text with the same filename as PDF file.
    :param text: str
        The PDF's content
    :param filename: str
        PDF's filename
    :param out: str
        Path where to store the file.
    :return: None
    """

    # get list of pdf files

    with open(os.path.join(out, f"{filename}.txt"), "w") as text_file:
        text_file.write(text)


def save_csv(data: List[str], path: str):
    """
    Saves csv annotation file.

    format:
    |====================================================================|
    |   filename   |   date   |   article_id   |   sentence   |   label  |
    |====================================================================|
    |--------------|----------|----------------|--------------|----------|
    |--------------|----------|----------------|--------------|----------|
    |--------------|----------|----------------|--------------|----------|
    |--------------|----------|----------------|--------------|----------|
    |====================================================================|

    :param data: str
        Sentence/clause
    :param path: str
        Path where to store csv file
    :return: None
    """

    # header of csv file
    header = ['filename', 'date', 'article_id', 'sentence', 'label']

    # getting the mode
    mode = 'a' if os.path.exists(path) else 'w'

    # open the file in the write mode
    with open(path, mode, encoding='UTF8') as f:
        # create the csv writer
        writer = csv.writer(f)

        # if write mode(file not exist, then add header row)
        if os.stat(path).st_size == 0:
            # write the header
            writer.writerow(header)

        # write the data
        writer.writerow(data)

    # close the file
    f.close()


if __name__ == "__main__":
    save_to_text('hello', 'done', '../../data/preprocessed/')