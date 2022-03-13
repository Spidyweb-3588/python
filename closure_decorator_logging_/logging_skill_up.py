import logging
logging.basicConfig(level=logging.INFO)

def hap(a, b):
    ret = a + b
    logging.info(f"input: {a} {b}, output={ret}")
    return ret

result = hap(3, 4)

#로거 객체를 만들어 로깅
log = logging.getLogger(__name__)

a = 3
b = 4
log.critical("%d + %d = %d", a, b, a+b)
log.error("%d + %d = %d", a, b, a+b)
log.warning("%d + %d = %d", a, b, a+b)
log.info("%d + %d = %d", a, b, a+b)
log.debug("%d + %d = %d", a, b, a+b) #레벨을 logging.info로 지정했기 때문에 그보다 낮은 레벨인 debug는 출력되지 않는다.
