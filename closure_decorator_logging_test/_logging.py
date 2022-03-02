import logging
logging.basicConfig(level=logging.INFO)

def hap(a, b):
    ret = a + b
    logging.info(f"input: {a} {b}, output={ret}")
    return ret

result = hap(3, 4)

"""log = logging.getLogger(__name__)

a = 3
b = 4
log.info("%d + %d =", a, b)"""
