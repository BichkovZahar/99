import logging #стандартний
logging.basicConfig(level = logging.DEBUG , format = '%(asctime)s - %(levelname)s - %(message)s')
logging.debug("debug")
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")