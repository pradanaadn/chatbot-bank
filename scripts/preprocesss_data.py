from pathlib import Path

from os import listdir, path
from loguru import logger
import pymupdf4llm

RAW_DATA_FOLDER = Path.cwd().joinpath("data", "raw")
RAW_DATA_LIST = listdir(RAW_DATA_FOLDER)
RAW_DATA_LIST_PATH = [RAW_DATA_FOLDER.joinpath(raw_data) for raw_data in RAW_DATA_LIST]

PROCESSED_DATA_FOLDER = Path.cwd().joinpath("data", "processed")


try:
    
    for pdf_file in RAW_DATA_LIST_PATH:
        logger.info(f"Document {pdf_file.name} is still converting to Markdown.")
        md_text = pymupdf4llm.to_markdown(pdf_file)
        markdown_file_name = path.splitext(pdf_file.name)[0]
        OUTPUT_PATH = PROCESSED_DATA_FOLDER.joinpath(f"{markdown_file_name}.md")
        OUTPUT_PATH.write_bytes(md_text.encode())
        logger.success(f"Success Converting Document {markdown_file_name} to Markdown.")
except Exception as e:
    logger.exception(f"Found {e}")

