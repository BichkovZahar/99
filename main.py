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
#факторіал числа
def factorial(n):
    logging.info(f"Розпочато обчислення факторіалу числа{n}")
    rezult = 1
    for i in range(1 , n + 1):
        rezult *= i  #1*2*3...
    logging.info(f"Обчислення факторіалу Резутьтат {rezult}")
    return rezult
logging.basicConfig(level= logging.INFO)
factorial(5)