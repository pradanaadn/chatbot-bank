from pathlib import Path
from os import path
from loguru import logger
import pymupdf4llm


def preprocess_data(pdf_file_directory: list[Path], output_file_directory: Path):
    try:
        for pdf_file in pdf_file_directory:
            logger.info(f"Document {pdf_file.name} is still converting to Markdown.")
            md_text = pymupdf4llm.to_markdown(pdf_file)
            markdown_file_name = path.splitext(pdf_file.name)[0]
            OUTPUT_PATH = output_file_directory.joinpath(f"{markdown_file_name}.md")
            OUTPUT_PATH.write_bytes(md_text.encode())
            logger.success(
                f"Success Converting Document {markdown_file_name} to Markdown."
            )
    except Exception as e:
        logger.exception(f"Found {e}")
