import time
import RPi.GPIO as GPIO
def GPIOset():
    GPIO.setmode(GPIO.BOARD) #pin numaralandırması
    GPIO.setup(11, GPIO.OUT) #kullanılan pin

def GPIOexe():
    GPIO.output(11, GPIO.HIGH) #piksel sayısı 1000 den fazlaysa pin11 e sinyal gider
    time.sleep(1) #sn cinsinden bekleme
    GPIO.output(11, GPIO.LOW)





