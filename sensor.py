import RPi.GPIO as GPIO
import time
import requests

# Setup GPIO pins
TRIG = 23
ECHO = 24
LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # Distance in cm
    return round(distance, 2)

def send_obstacle_update(distance):
    if distance < 20:  # If obstacle is detected within 20 cm
        GPIO.output(LED_PIN, True)  # Turn on LED
        # Adjust coordinates based on your grid
        response = requests.get("http://<YOUR_COMPUTER_IP>:5000/add_obstacle/1/1")
        print("Obstacle detected, updating server:", response.json())
    else:
        GPIO.output(LED_PIN, False)  # Turn off LED

try:
    while True:
        distance = get_distance()
        print("Distance:", distance, "cm")
        send_obstacle_update(distance)
        time.sleep(1)

except KeyboardInterrupt:
    print("Measurement stopped by user")
    GPIO.cleanup()
