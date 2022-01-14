import os
import platform


def get_os() -> str:
    """
    Get the operating system running the script.
    :return: str, Linux/ or Windows for linux/ or windows base operating system,
    """
    return platform.system()


def clear_screen() -> None:
    """
    Clears screen depending on operating systems.
    :return: None
    """

    operating = get_os()
    if operating == 'Linux':
        os.system('clear')
    elif operating == 'Windows':
        os.system('cls')
    else:
        ValueError('Cannot detect your operating system !')


if __name__ == "__main__":
    clear_screen()
