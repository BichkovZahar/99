import logging #стандартний
logging.basicConfig(level = logging.DEBUG ,
                    filename = "logs.log" ,
                    filemode = 'w' ,
                    format ='%(asctime)s - %(levelname)s - %(message)s')
logging.debug("debug")
logging.info("info")
logging.error("error")
logging.warning("warning")
logging.critical("critical")

try:
    print(10 / 0)
except Exception:
    logging.exception("GG")
