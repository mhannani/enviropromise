"""

Data collection:
================

Data was collected from ecolex.org database, from moroccan legal documents about
regularization on plastic bags and protection of marine biodiversity of Mediterranean
and Pacific oceans.

Different approach will be used to target the problem of feature extraction,
specifically, bans.json and sanction from legal documents:


Machine Learning model:
=======================

To create a model for information extraction model we've:

    (1) Use of different deep learning models
        A. Produce a dense vector representation of texts/ or text vectorization:
            The experiments will be conducted using GloVe and FastText word embeddings.

        B. Then sequence labelling:
            Sequence labelling will be handled by different architecture, BiLSTM-based,
            BiGRU-based and CNN-based architectures.

    (2) Use Transfer learning, using Google's BERT:
        Using Google's Bidirectional Encoder Representation from Transformers(BERT)
        language model since it achieve the state-of-the-art result on various NLP tasks
        particularly in tasks involving sequence labelling.

"""