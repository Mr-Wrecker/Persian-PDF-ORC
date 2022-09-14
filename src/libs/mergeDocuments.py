import os
from pydoc import doc
from docx import Document
from docxcompose.composer import Composer
from ._CONST import OCR_Path


def Combine(name):
    print('Combine Documents ...')

    docs = []
    # Iterate directory
    for path in os.listdir(OCR_Path):
        # check if current path is a file
        if os.path.isfile(os.path.join(OCR_Path, path)):
            docs.append(f"{OCR_Path}/{path}")

    # Sort Pages
    docs = sorted(docs)

    composed = f"{OCR_Path}/{name}.docx"

    # Merge Documents
    result = Document(docs[0])
    result.add_page_break()
    composer = Composer(result)

    for i in range(1, len(docs)):
        doc = Document(docs[i])

        if i != len(docs) - 1:
            doc.add_page_break()

        composer.append(doc)

    composer.save(composed)
