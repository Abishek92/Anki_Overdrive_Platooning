import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24
while True:
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False)
    time.sleep(.5)

    GPIO.output(TRIG, True)
    time.sleep(0.5)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance1 = pulse_duration * 17150

    distance1 = round(distance1,5)

    GPIO.output(TRIG, False)
    time.sleep(1)

    GPIO.output(TRIG, True)
    time.sleep(0.5)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
      pulse_start = time.time()

    while GPIO.input(ECHO)==1:
      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance2 = pulse_duration2 * 17150

    distance2 = round(distance2,5)


    Relative_velocity = (distance2-distance1)/1

    Velocity = 10*Relative_velocity
    Distance = distance2*10

    print "Velocity", Relative_velocity,"mm/sec"
    print "Distance:",Distance,"mm"
    
    nominal_distance = 100 

    Required_Velocity = nominal_distance - Distance*kp + Relative_velocity*kd

    print "Current Speed:",Required_Velocity,"mm/sec"
    file=open("setspeed.txt","w")
    file.write("%d" % speed)
    file.close()
GPIO.cleanup()

