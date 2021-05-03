import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

servo = GPIO.PWM(11,50)
servo.start(0)
time.sleep(1)
duty = 2

while duty<=12:
	servo.ChangeDutyCycle(duty)
	time.sleep(1)
	duty = duty+1
time.sleep(2)

while duty>=0:
	servo.ChangeDutyCycle(duty)
	time.sleep(0.5)
	duty=duty-1
servo.stop()
GPIO.cleanup()
print('done')

