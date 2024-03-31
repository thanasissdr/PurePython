import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("log.txt", mode="w+")

# Set Formatter
c_format = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
f_format = logging.Formatter("%(name)s-%(levelname)s-%(message)-s")

c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers
logger.addHandler(c_handler)
logger.addHandler(f_handler)


if __name__ == "__main__":
    logger.info("Hello world")
