import os.path
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
    for json in jsons:
        # Parse the json file
        sentences = parse_json(os.path.join(JSON_OUT, json))

        for sentence in sentences:
            pass


if __name__ == "__main__":
    annotate_and_save(directory=JSON_OUT, data_ready_path=DATA_READY_OUT)
