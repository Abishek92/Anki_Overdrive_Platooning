import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24
while True:
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    time.sleep(1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance,5)

    Distance = distance*10
    print "Distance:",Distance,"mm"
    Velocity = 0

    if Distance < 150:
      Velocity = 0
    elif Distance < 190:
      Velocity = 100
    elif Distance < 200:
      Velocity = 150
    elif Distance < 250:
      Velocity = 200
    elif Distance < 300:
      Velocity = 300
    elif Distance < 400:
      Velocity = 400
    elif Distance < 500:
      Velocity = 450
    elif Distance > 500:
      Velocity = 300
    # nominal_distance = 100 

    # Required_Velocity = nominal_distance - Distance*kp + Relative_velocity*kd

    print "Current Speed:",Velocity,"mm/sec"
    file=open("setspeed.txt","w")
    file.write("%d" % Velocity)
    file.close()
GPIO.cleanup()
