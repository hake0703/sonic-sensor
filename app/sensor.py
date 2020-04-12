import RPi.GPIO as GPIO
import time

__sonic_speed_cm = 34300 # sonic speed (34300 cm/s)

class SonicSensor:

	def __init__(self, trigger_gpio = 7, echo_gpio = 11, gpio_type = GPIO.BOARD):
		self.gpio_trigger = trigger_gpio
		self.gpio_echo = echo_gpio

		GPIO.setmode(gpio_type)
		GPIO.setup(self.gpio_trigger, GPIO.OUT)
		GPIO.setup(self.gpio_echo, GPIO.IN)

def get_signal_travel_time(sonic_sensor):
	GPIO.output(sonic_sensor.gpio_trigger, True)

	time.sleep(0.00001)
	GPIO.output(sonic_sensor.gpio_trigger, False)
	StartTime = time.time()
	StopTime = time.time()

	while GPIO.input(sonic_sensor.gpio_echo) == 0:
		StartTime = time.time()

	while GPIO.input(sonic_sensor.gpio_echo) == 1:
		StopTime = time.time()

	TimeElapsed = StopTime - StartTime
	return TimeElapsed

def get_distance_centimeters(time_elapsed):
	return (time_elapsed * __sonic_speed_cm)/2 # divide by 2, due to bi-directional travel

def get_distance_inches(time_elapsed):
	distance_cm = get_distance_centimeters(time_elapsed)
	inches_divisor = 2.54
	return (distance_cm)/(inches_divisor)

# If Module is run directly from cmd line, execute as stand alone app.
if __name__ == '__main__':
	print("Starting application...")
	sensor = SonicSensor()
	try:
		while True:
			travel_time = get_signal_travel_time(sensor)
			dist = get_distance_inches(travel_time)			
			print("Distance = %.3f inches" % dist)
			time.sleep(1)
	except KeyboardInterrupt:
			print("Measurement Stopped by User..")
			GPIO.cleanup()