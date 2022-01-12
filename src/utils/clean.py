import re
from typing import List


def clean_txt(text: str) -> List[str]:
    """
    Make cleaning of text.
    :param text: str
        Input text.
    :return: str
        Output cleaned text.
    """

    # Define entities
    alphabets = "([A-Za-z])"
    prefixes = "(M|Mme|Dr|Drs)[.]"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = r'http\S+'
    starters = "(il\s|elle\s|elles\s|ils\s|mienne\s|tienne\s|nous\s|main\s|malgre\s|ceci\s|cela\s|quelque)"

    # Pas text with spaces
    text = " " + text + "  "

    text = re.sub(prefixes,"\\1<prd>",text)

    # replace newline
    text = text.replace("\n", " ")

    text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)

    # replace websites
    text = re.sub(websites, '', text)

    # substitute acronym followed by starter and replace them with <stop> token
    text = re.sub(acronyms+" "+starters, "\\1<stop> \\2",text)

    # pre-add space to ", /, ! and ?
    if "”" in text: text = text.replace(".”", "”.")
    if "\"" in text: text = text.replace(".\"", "\".")
    if "!" in text: text = text.replace("!\"", "\"!")
    if "?" in text: text = text.replace("?\"", "\"?")

    # replace ., ?, ! and <prd> tokens with <stop> token
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")

    # split the text using <stop> delimiter
    sentences = text.split("<stop>")

    # discard the last element as it's just a whitespace
    sentences = sentences[:-1]

    # remove trailing and leading whitespaces
    sentences = [s.strip() for s in sentences]

    return sentences


if __name__ == "__main__":
    txt = 'M. mohamed, je suis tres heureux.' \
          'et voila ma finalite https://mhannani.com !'
    print('original text: ', txt)
    print('cleaned text: ', clean_txt(txt))
