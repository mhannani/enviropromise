from tqdm import tqdm
from os import path
from src.config import *
from src.utils.find import find_json
from src.utils.parse import parse_json


def annotate_and_save(directory: str, data_ready_path: str) -> None:
    """
    Annotates and saves to file.
    :return: None
    """

    # get the json files
    jsons = find_json(directory)

    # loop through all json files
    for i, json in enumerate(jsons):
        # articles_bar = tqdm(total=len(jsons), bar_format='{l_bar}{bar:10}{r_bar}',
        #              unit='articles', ncols=200, mininterval=0.5, colour='#00ff00')

        # Parse the json file
        _, _, _, _, sentences = parse_json(path.join(JSON_OUT, json))
        articles_bar = tqdm(total=len(sentences), bar_format='{l_bar}{bar:10}{r_bar}',
                            unit='articles', ncols=200, mininterval=0.5, colour='#00ff00')

        for j, sentence in enumerate(sentences):
            # print(sentence)
            annotation = input('\nWhat is this (0): ban or (1): sanction ? Enter to neglect it')

            # print(annotation)
            # update the progress bar
            articles_bar.set_postfix(article=f" {i}/{len(jsons)}", refresh=True)
            articles_bar.update()

        articles_bar.close()


if __name__ == "__main__":
    annotate_and_save(directory=JSON_OUT, data_ready_path=DATA_READY_OUT)
