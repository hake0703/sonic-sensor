### Use this class to send power through a GPIO Pin
import RPi.GPIO as GPIO
import time

class LED:

    def __init__(self, gpio_pin, gpio_type = GPIO.BOARD):
        self.gpio_pin = gpio_pin
        GPIO.setmode(gpio_type)
        GPIO.setwarnings(False)
        GPIO.setup(self.gpio_pin, GPIO.OUT)

    def trigger_led_on(self):
        print("LED on")
        GPIO.output(self.gpio_pin, GPIO.HIGH)
    
    def trigger_led_off(self):
        print("LED off")
        GPIO.output(self.gpio_pin, GPIO.LOW)
