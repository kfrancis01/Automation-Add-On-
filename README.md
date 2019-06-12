# Automation-Add-On
Automatically execute python scripts, collect data, and create live graphs depending on an object's position.  

## How It Works
This project was designed as an add on for my research project. I needed to determine the placement of an object on a table after it was rolled into place. In order to accomplish this I used an Arduino compatible laser and photoresistor to create a trip wire. This was combined with a ultrasound distance sensor to determine and print the distance to the serial. 

The second phase involved translating the distance into an approximate location of the object on the table and having a phone app text to speech feature deliver an appropriate response. To accomplish this a Raspberry Pi was connected through USB to the Arduino. A Python script executed on the Raspberry Pi would determine the approximate placement and execute a secondary script that communicates to a phone app. The phone app would then make an appropriate response to the input. 

To make life easier for the researcher the distance collected is recorded on an .xlxs file in the background and can be opened after the experiment is completed. The researcher can also track the progress using live graphs on the Raspberry Pi that update after receiving new distance readings.

## Getting Started
This project requires an app created through MIT App Inventor that can not be shared since it was a part of my undergraduate research. However, any executable Python code can take the place of the one presently being used. 
```

```
## Required Libraries and Packages 

#### Raspberry Pi
I will assume that pip has previously been installed onto the Raspberry Pi.
In order to create the graphs the matplotlib library was utilized
```
pip3 install matplotlib --user
```
An .xlxs can later be downloaded onto a laptop and opened using excel. In order to create a formattable table of data openpyxl was installed
```
pip3 install openpyxl --user
```
In order to view the .xlxs file from the Raspberry Pi
```
sudo apt-get install libreoffice 
```
#### Arduino
The Arduino code was created using the online Arduino Editor IDE. Using this platform the Arduino zip folder simple needs to be uploaded. In order for your Arduino device to be recognized you must download the Arduino create agent to your PC.

[Arduino Create Agent](https://create.arduino.cc/getting-started/plugin)

## Running the Program
Download the Distance_Project onto the Arduino and connect it to the Raspberry using the usb. 
After installing the Python code onto the Raspberry Pi Desktop you must first make it executable from the command line.
Navigate to the Desktop in the command line then use
```
chmod +x DistanceProject.py
```
This will allow you to simply locate the file in the Raspberry Pi Desktop and execute by double clicking on it. 
