# Automation-Add-On-
Automatically execute python scripts, collect data, and create live graphs from Arduino distance sensor outputs 
This project was designed as an add on for my research project. I needed to determine the placement of an object on a table after it was rolled into place. In order to accomplish this I used an Arduino compatible laser and photoresistor to create a trip wire. This was combined with a ultrasound distance sensor to determine and print the distance to the serial. 
The second phase involved translating the distance into an approximate location of the object on the table and having a phone app deliver an appropriate response. To accomplish this a Raspberry Pi was connected through USB to the Arduino. A Python script executed on the Raspberry Pi would determine the approximate placement and execute a secondary script that communicates to a phone app. The phone app would then respond to the input. 
To make life easier for the researcher the distance collected is recorded on an .xlxs file in the background and can be opened after the experiment. The researcher can also track the progress using live graphs. 

