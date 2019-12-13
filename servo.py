import RPi.GPIO as gpio
from time import sleep

class Servo_control:
  def __init__(self, pin=12):
    self.pin = pin
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    gpio.setup(pin. gpio.OUT)
    self.pwm = gpio.PWM(pin, 50)
    self.pwm.start(7.5)
  def set_degree(self, alpha=180.0):
    duty_cycle = float(alpha/18.0)
    duty_cycle += 2.5
    self.pwm.ChangeDutyCycle(duty_cycle)
  def servo_quit(self)
    self.pwm.stop()
    
