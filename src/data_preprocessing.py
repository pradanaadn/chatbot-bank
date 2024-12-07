from pathlib import Path
from os import listdir
from scripts.preprocesss_data import preprocess_data

RAW_DATA_PDF_FOLDER = Path.cwd().joinpath("data", "raw", "pdf")
RAW_DATA_LIST_PDF = listdir(RAW_DATA_PDF_FOLDER)

RAW_DATA_LIST_PDF_PATH = [
    RAW_DATA_PDF_FOLDER.joinpath(raw_data) for raw_data in RAW_DATA_LIST_PDF
]

PROCESSED_DATA_FOLDER = Path.cwd().joinpath("data", "processed")


if __name__ == "__main__":
    preprocess_data(
        pdf_file_directory=RAW_DATA_LIST_PDF_PATH,
        output_file_directory=PROCESSED_DATA_FOLDER,
    )
