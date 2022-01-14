from tqdm import tqdm
from os import path
from src.config import *
from src.utils.format import show_query
from src.utils.save import save_csv
from src.utils.find import find_json
from src.utils.parse import parse_json
from src.utils.io import clear_screen


def annotate_and_save(directory: str, data_ready_path: str) -> None:
    """
    Annotates and saves to file.
    :return: None
    """

    # get the json files
    jsons = find_json(directory)

    # clear screen
    clear_screen()

    # data holder
    data = []

    # loop through all json files
    for i, json in enumerate(jsons):
        # Parse the json file
        filename, date, n_article, _, sentences = parse_json(path.join(JSON_OUT, json))
        p_bar = tqdm(total=len(sentences), bar_format='{l_bar}{bar:10}{r_bar}',
                            unit='sentence', ncols=200, mininterval=0.5, colour='#00ff00')

        for j, sentence in enumerate(sentences):
            show_query(sentence)
            response = input('\nWhat is this (0): ban or (1): sanction ? Enter to neglect it: ')

            try:
                label = int(response)
                if label in [0, 1]:
                    record = [filename, date, n_article, sentence, label]
                    # save clause with its label to file
                    save_csv(record, data_ready_path)
            except ValueError:
                pass

            # clear screen
            clear_screen()

            # modify the progress bar
            p_bar.set_postfix(article=f" {i+1}/{len(jsons)}", refresh=True)

            # update the progress bar
            p_bar.update()

        p_bar.close()


if __name__ == "__main__":
    annotate_and_save(directory=JSON_OUT, data_ready_path=DATA_READY_OUT)
