import RPi.GPIO as GPIO  ## GPIO library
import time   ## Time library


##declaring pins and board
GPIO.setmode(GPIO.BOARD)  
GPIO.setup(14,GPIO.OUT)


try:
    while 1:
        GPIO.output(14,GPIO.HIGH)   
        time.sleep(0.5) ## time delay for 0.5 seconds
        GPIO.output(14,GPIO.LOW)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
