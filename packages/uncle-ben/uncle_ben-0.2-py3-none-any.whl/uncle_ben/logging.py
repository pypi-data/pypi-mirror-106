import sys
import logging

logger = logging.getLogger("uncle-ben")
logger.setLevel(logging.INFO)


def enable_debug():
    log_model = "%(asctime)s -%(levelname)10s - " \
                "%(module)s.%(funcName)s.L_%(lineno)d: %(message)s"

    formatter = logging.Formatter(log_model, datefmt='%Y-%m-%d %H:%M:%S')

    debug = logging.StreamHandler(sys.stderr)
    debug.setLevel(logging.DEBUG)
    debug.setFormatter(formatter)
    logger.addHandler(debug)
    logger.setLevel(logging.DEBUG)
