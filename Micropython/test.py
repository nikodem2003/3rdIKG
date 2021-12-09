def connect():
	import network

	ssid = "TN_wifi_D7AD79"
	password = "LGCWV4AYG7"

	station = network.WLAN(network.STA_IF)

	if station.isconnected() == True:
		print("Already connected")
		return

	station.active(True)
	station.connect(ssid, password)

	while station.isconnected() == False:
		pass

	print("Connection successful")
	print(station.ifconfig())

def led():
	import time
	import machine
	blueled = machine.Pin(2, machine.Pin.OUT)

	# Blink 10 times
	for i in range(1,11):
	    blueled.value(0)
	    time.sleep(0.5)
	    blueled.value(1)
	    time.sleep(0.5)

	print("DONE!")

def pwm():
	from machine import Pin
	from machine import PWM
	import time

	# Set our pin 2 to PWM
	pwm = PWM(Pin(2))

	# Frequency = 100hz
	pwm.freq(100)

	while 1:
	  # Brightness between 0 and 1023
	  for brightness in range (0, 1023, 100):
	    pwm.duty(brightness)
	    print(brightness)
	    time.sleep(0.1)

	  # Brightness between 1023 and 0
	  for brightness in range (1023, 0, -100):
	    pwm.duty(brightness)
	    print(brightness)
	    time.sleep(0.1)

def anal():
	# Complete project details at https://RandomNerdTutorials.com

	from machine import Pin, ADC
	from time import sleep

	pot = ADC(0)

	while True:
	  pot_value = pot.read()
	  print(pot_value)
	  sleep(0.1)
	  break

#boot sequence
def bootup():
	print("step one starts")
	connect()
	run()
#	import webrepl_setup

def run():
	print("run starts")
	while True:
		#led()
		pwm()
		#print("working")
		#anal()
		#break

#on boot: 
bootup()


