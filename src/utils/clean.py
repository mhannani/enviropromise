import logging
import os
import re
from typing import List, Tuple


def clean_txt(text: str) -> Tuple[List[str], str, str, str]:
    """
    Make cleaning of text.

    :param text: str
        Input text or Filename of file containing text.

    :return: tuple(List[str], str, str, str)
        Output cleaned text, Filename, date, article number
    """
    # if the input is plain-text
    filename = None
    date = None
    n_article = None

    # Define entities
    alphabets = "([A-Za-z])"
    prefixes = "(M|Mme|Dr|Drs)[.]"
    websites = r'http\S+'

    # load file is from_file is supplied
    if os.path.isfile(text):
        # Get the filename
        filename = os.path.splitext(os.path.basename(text))[0]

        # read the file
        with open(text, 'r') as stream:
            text = stream.read()

    # Pad text with spaces
    text = " " + text + "  "

    text = re.sub(prefixes, "\\1<prd>",text)

    # replace newline
    text = text.replace("\n", " ")

    text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)

    # remove hex characters
    text = re.sub(r'[^\x00-\x7f]', r'', text)

    # remove the \" after the article number
    text = re.sub(r'\"', r'', text)

    # Get the date

    # replace websites
    text = re.sub(websites, '', text)

    # pre-add space to ", /, ! and ?
    if "”" in text:
        text = text.replace(".”", "”.")
    if "\"" in text:
        text = text.replace(".\"", "\".")
    if "!" in text:
        text = text.replace("!\"", "\"!")
    if "?" in text:
        text = text.replace("?\"", "\"?")

    # replace ., ?, ! and <prd> tokens with <stop> token
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")

    # split the text using <stop> delimiter
    sentences = text.split("<stop>")

    try:
        date = re.search(r'\d{1,2}-\d{1,2}-\d{4}', text).group(0)
    except AttributeError as err:
        print('Cannot extract date from current document')
        print('error message: ', err)

    try:
        n_article = re.search('NO? (\d+)', text).group(1)
    except AttributeError as err:
        print('Cannot extract n_article from current document')
        print('error message: ', err)

    # discard the last element as it's just a whitespace
    sentences = sentences[:-1]
    # remove trailing and leading whitespaces
    sentences = [s.strip() for s in sentences]

    return sentences, filename, date, n_article


if __name__ == "__main__":
    file_name = '../../data/interim/Mor106711.txt'
    print('cleaned text: ', clean_txt(file_name))
