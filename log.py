import logging

logger = logging.getLogger(__name__)


def log(name):
    _log = logging.getLogger(name)
    _log.setLevel("DEBUG")

    # Create handlers
    c_handler = logging.StreamHandler()

    # Create formatters and add it to handlers
    # Configure the logger
    simple_format = logging.Formatter(
        "%(asctime)s [%(funcName)s() +%(lineno)d]: %(levelname)-8s %(message)s",
        datefmt="%b-%d %H:%M:%S%Z"
    )
    c_handler.setFormatter(simple_format)

    # Add handlers to the logger
    _log.addHandler(c_handler)

    return _log


# Use this variable for global project
logger = log(__name__)
