import logging
import os

logger = logging.getLogger(__name__)


def isValidCSV(file: str) -> bool:
    ext = os.path.splitext(file)[-1].lower()
    return os.path.isfile(file) and (ext == ".csv")
