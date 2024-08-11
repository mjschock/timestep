"""Read PDF files using PyMuPDF library."""

from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Union

from llama_index.core.readers.base import BaseReader
from llama_index.core.schema import Document
import numpy as np
import pymupdf


def extract_from_images_with_rapidocr(
    images: Sequence[Union[Iterable[np.ndarray], bytes]],
) -> str:
    """Extract text from images with RapidOCR.

    Args:
        images: Images to extract text from.

    Returns:
        Text extracted from images.

    Raises:
        ImportError: If `rapidocr-onnxruntime` package is not installed.
    """
    try:
        from rapidocr_onnxruntime import RapidOCR

    except ImportError:
        raise ImportError(
            "`rapidocr-onnxruntime` package not found, please install it with "
            "`pip install rapidocr-onnxruntime`"
        )

    ocr = RapidOCR()
    text = ""

    for img in images:
        result, _ = ocr(img)
        if result:
            result = [text[1] for text in result]
            text += "\n".join(result)

    return text

# See:
# https://api.python.langchain.com/en/latest/document_loaders/langchain_community.document_loaders.pdf.PyMuPDFLoader.html#langchain_community.document_loaders.pdf.PyMuPDFLoader
# https://api.python.langchain.com/en/latest/document_loaders/langchain_community.document_loaders.parsers.pdf.PyMuPDFParser.html
class PyMuPDFReader(BaseReader):
    """Read PDF files using PyMuPDF library."""

    def __init__(
        self,
        extract_images: bool = False,  
    ) -> None:
        super().__init__()

        self.extract_images = extract_images

    def load_data(
        self,
        # file_path: Union[Path, str],
        file: Path,
        metadata: bool = True,
        extra_info: Optional[Dict] = None,
    ) -> List[Document]:
        """Loads list of documents from PDF file and also accepts extra information in dict format."""
        # return self.load(file_path, metadata=metadata, extra_info=extra_info)
        return self.load(file, metadata=metadata, extra_info=extra_info)

    def load(
        self,
        # file_path: Union[Path, str],
        file: Path,
        metadata: bool = True,
        extra_info: Optional[Dict] = None,
    ) -> List[Document]:
        """Loads list of documents from PDF file and also accepts extra information in dict format.

        Args:
            file_path (Union[Path, str]): file path of PDF file (accepts string or Path).
            metadata (bool, optional): if metadata to be included or not. Defaults to True.
            extra_info (Optional[Dict], optional): extra information related to each document in dict format. Defaults to None.

        Raises:
            TypeError: if extra_info is not a dictionary.
            TypeError: if file_path is not a string or Path.

        Returns:
            List[Document]: list of documents.
        """
        # import fitz

        # check if file_path is a string or Path
        # if not isinstance(file_path, str) and not isinstance(file_path, Path):
        if not isinstance(file, str) and not isinstance(file, Path):
            raise TypeError("file_path must be a string or Path.")

        # open PDF file
        # doc = fitz.open(file_path)
        # doc = fitz.open(file)
        doc = pymupdf.open(file)

        # if extra_info is not None, check if it is a dictionary
        if extra_info:
            if not isinstance(extra_info, dict):
                raise TypeError("extra_info must be a dictionary.")

        # if metadata is True, add metadata to each document
        if metadata:
            if not extra_info:
                extra_info = {}
            extra_info["total_pages"] = len(doc)
            # extra_info["file_path"] = str(file_path)
            extra_info["file_name"] = file.name

            # return list of documents
            return [
                Document(
                    text=self.extract_text(doc, page),
                    extra_info=dict(
                        extra_info,
                        **{
                            "source": f"{page.number+1}",
                        },
                    ),
                )
                for page in doc
            ]

        else:
            return [
                Document(
                    text=self.extract_text(doc, page), extra_info=extra_info or {}
                )
                for page in doc
            ]

    def extract_text(self, doc, page):
        text = page.get_text().encode("utf-8")

        if not text:
            print('Page text is empty; running OCR...')

            try:
                text = page.get_textpage_ocr().encode("utf-8")

            except RuntimeError as e:
                print(e)
                print("Running OCR with RapidOCR instead...")

                text = self._extract_images_from_page(doc, page)

        return text

    def _extract_images_from_page(
        # self, doc: fitz.fitz.Document, page: fitz.fitz.Page
        self, doc: pymupdf.Document, page: pymupdf.Page,
    ) -> str:
        """Extract images from page and get the text with RapidOCR."""
        if not self.extract_images:
            return ""

        # import fitz

        img_list = page.get_images()
        imgs = []

        for img in img_list:
            xref = img[0]
            # pix = fitz.Pixmap(doc, xref)
            pix = pymupdf.Pixmap(doc, xref)
            imgs.append(
                np.frombuffer(pix.samples, dtype=np.uint8).reshape(
                    pix.height, pix.width, -1
                )
            )

        return extract_from_images_with_rapidocr(imgs)
