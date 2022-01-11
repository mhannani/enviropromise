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

if __name__ == "__main__":
    save_to_text('hello', 'done', '../../data/preprocessed/')