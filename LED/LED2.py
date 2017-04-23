import wiringpi
from time import sleep
wiringpi.wiringPiSetup()
wiringpi.pinMode(0, 1)
wiringpi.digitalWrite(0,1)
sleep(20)
wiringpi.digitalWrite(0,0)
wiringpi.pinMode(0,0)
