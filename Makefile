download:
	wget -i ./data/external/PDFs.txt -P ./data/external/PDFs/
preprocess:
	python preprocess_and_save.py