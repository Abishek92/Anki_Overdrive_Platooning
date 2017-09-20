# Anki Overdrive Platooning
Welcome to the Anki_Overdrive_Platooning wiki!

Description:

Utilized Anki's Overdrive cars to implement Control theory techniques.
Modified the SDK in order to bypass the command prompt.
The SDK will speed values continuously from a text file instead of typing it in the terminal.
Original SDK: This is a modified version of Anki's Drive SDK which can be found at:

https://github.com/anki/drive-sdk

Installing on Raspberry PI:

This SDK is to be built and compiled on a Raspberry Pi (instead of a PC running Ubuntu) fitted with an Ultrasonic Sensor.
The tutorial on how to build the SDK is given below:
The process is identical to building the Anki-Drive-SDK:
https://github.com/anki/drive-sdk/wiki/Getting-Started-on-Ubuntu

Raspberry Pi and Python:

The Ultrasonic sensor is connected to the GPIO pins on the Raspberry Pi.
The code for the Ultrasonic sensor is given in Ultrasonic.py
This setup is fitted on the cars (Excluding the lead car, which is controlled by a PC running Linux)
The code includes a PD controller that calculates the required speed to maintain a nominal distance
Once the code is executed, it continuously measures the distance between the two cars and writes the required speed to a text file.
The car running the modified SDK will continuously execute the speed command and read the new values from the text file.
