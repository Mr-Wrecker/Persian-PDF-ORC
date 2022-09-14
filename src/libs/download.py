import requests
from ._CONST import OCR_Path
from .clean import Cleaner


def downloader(url, name):
    Cleaner(OCR_Path, False)

    name = f"{name}.txt"
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(f"{OCR_Path}/{name}", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return name
