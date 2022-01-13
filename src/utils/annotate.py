def annotate_clause(clause: str) -> int:
    """
    Annotate the given clause/sentence

    Part of future work:
    ====================

    The process of annotating data is overwhelming and time-consuming specially for large amount of corpus,
    and hence will be annotated using similarity search and sentence embeddings.

    :param clause: str
        A sentence or a clause to be annotated.
    :return: int
        The class of the clause, 0: for ban and 1 for sanction.
    """

    cls = 0

    return cls


if __name__ == "__main__":
    ex_clause = "L'UE a prolongé les sanctions qui visent la Russie jusqu'à la fin du mois de janvier 2016."
    annotate_clause(ex_clause)
