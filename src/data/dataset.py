from os.path import join
from torch.utils.data import Dataset
import pandas as pd


class LegalDataset(Dataset):
    """
    Legal dataset, for sentence classification.
    """

    def __init__(self, csv_file: str, root_dir: str) -> None:
        """
        The class constructor.
        :param csv_file: str
            The csv filename.
        """

        self.csv_path = join(root_dir, csv_file)
        self.root_dir = root_dir
        print(self.csv_path)
        self.data = pd.read_csv(self.csv_path)

    def __getitem__(self, item: int):
        """
        Get sample at index `item` in the dataset.
        :param item: int
            Index of sample to be returned.
        :return: Tuple(str, str)
            Tuple of sentence along with its label(0 for bans, 1 for sanctions).
        """

        # get the sentence at `item` index
        sentence = self.data.loc[item, 'sentence']

        # get the label
        label = self.data.loc[item, 'label']

        return sentence, label

    def __len__(self) -> int:
        """
        Get the length of data.
        :return: int
            Length of data.
        """

        return len(self.data)


if __name__ == "__main__":
    legal_dataset = LegalDataset(csv_file='annotated.csv', root_dir='data/')
    print('__len__: ', legal_dataset.__len__(), 'samples')
    print(legal_dataset.__getitem__(0))