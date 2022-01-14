from colorama import init, Fore, Style


def show_query(sentence: str) -> None:
    """
    Show formatted sentence query for annotating process.
    :param sentence: str
        Sentence or clause.
    :return: None
    """

    # init window environment
    init()
    print(f'{Fore.GREEN} \n')
    print('****************************************************************************')
    print('*****')
    print(sentence)
    print('*****')
    print('****************************************************************************')
    print(f'{Style.RESET_ALL}')


if __name__ == "__main__":
    show_query('This is a test')
