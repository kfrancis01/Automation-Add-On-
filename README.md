# Automation Add-On
Automatically run commands, collect data, and create live graphs depending on an object's position.  

**NOTE: *This project was designed as a proof of concept since the full set up for appropriate testing was not available***

## How It Works
This project was designed as an add on for my research project. I needed to determine the placement of an object on a table after it was rolled into place. In order to accomplish this, I used an laser emitter and photoresistor to create a trip wire. This was combined with an ultrasound distance sensor to determine and print the distance to the serial. 

The second phase involved translating the distance into an approximate location of the object on the table and having a phone app text to speech feature deliver an appropriate response. To accomplish this a Raspberry Pi was connected through USB to the Arduino. Depending on the reading the commands used for the Pi to phone communication was activated. The phone app would then make an appropriate response to the input. 

To make life easier for the researcher the distance collected is recorded on an .xlxs file in the background and can be opened after the experiment is completed. The researcher can also track the progress using live graphs on the Raspberry Pi that update after receiving new distance readings.

## Getting Started
This project requires an app created through MIT App Inventor that cannot be shared. However, any Python command can be used in its place. 

  ![Possible Python Change](http://g.recordit.co/oakSKnxkT8.gif)

  ### Testing
  The Arduino code sends out distance measurements unless the laser beam is directed towards the photoresistor. No two photoresistors     work exactly the same so some manipulation may have to be done in the Arduino code.
  ```Python
  if (light < 900)
  ```
  print out the value for light and find the value given when the laser beam is directed towards the photoresistor. Then reset the         above portion of the code appropriately.
  
  ![Photoresistor Test](http://g.recordit.co/Nn9jbYphNq.gif) 

### Hardware
[Arduino Component Connections](https://www.tinkercad.com/things/4tLGjxeFeIk-funky-krunk-juttuli/editel?tenant=circuits)
* Arduino (Uniroi) Uno
* Raspberry Pi 3 B
* 2 pin anti-reverse cable
* Photoresistor
* Sunfounder Laser Emitter
* 10 ohm resistor
* HC-SR04 Ultrasonic Sensor
* Breadboard
* A male to B male USB cable

## Required Libraries and Packages 

#### Raspberry Pi
I will assume that pip has previously been installed onto the Raspberry Pi.
In order to create the graphs, the matplotlib library was utilized. In order to avoid permission error during installation append `--user` at the end.
```Python
>> pip3 install matplotlib --user
```
An .xlxs can later be downloaded onto a laptop and opened using excel. In order to create a formattable table of data openpyxl was installed
```Python
>> pip3 install openpyxl --user
```
Numpy for Python allows us to create and manipulate arrays
```Python
>> sudo apt-get install python3-numpy
```
In order to view the .xlxs file from the Raspberry Pi
```Python
>> sudo apt-get install libreoffice 
```
#### Arduino
The Arduino code was created using the online Arduino Editor IDE. Using this platform the Arduino zip folder simple needs to be uploaded. For your Arduino device to be recognized you must download the Arduino create agent to your PC.

[Arduino Create Agent](https://create.arduino.cc/getting-started/plugin)

## Running the Program
Download the Distance_Project onto the Arduino and connect it to the Raspberry using the USB. 
After installing the Python code onto the Raspberry Pi Desktop, you must first make it executable from the command line.
Navigate to the Desktop in the command line then use:
```Python
>> chmod +x DistanceProject.py
```
This will allow you to simply locate the file in the Raspberry Pi Desktop and execute by double clicking on it. 
You can end the program by closing the figure window or entering `ctrl + c`. Once the program has stopped an updated .xlxs file called DistanceRecorded will be uploaded to the desktop. Opening the file will show the time and date at the top left corner as well as the distances gathered.
