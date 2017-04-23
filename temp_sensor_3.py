import os
import glob
import time
import calendar
import time
from time import gmtime, strftime
import wiringpi
from time import sleep

wiringpi.wiringPiSetup()

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

print 'Date: '+ strftime("%d-%m-%Y %H:%M", gmtime()) + ', Temp: ' + str(read_temp()) + ' C'

if (read_temp()>20):
    wiringpi.pinMode(0,1)
    wiringpi.digitalWrite(0,1)
    sleep(10)
    wiringpi.digitalWrite(0,0)
    wiringpi.pinMode(0,0)
