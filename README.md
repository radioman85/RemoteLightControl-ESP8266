# RemoteLightControl-ESP8266
Release 0.1 (it is not doing so much at the time!)

In this Project the goal is to control any number of light nodes connected to the wifi (ESP8266) with my raspberry pi.

The textfile lights.txt contains discription of light object that should be controlled. As an example:

light_id: 1
requested_status: on
status: off

light_id: 2
requested_status: off
status: off

... and so on

With light_interface.py this file is read and the corresponding lights are turned on or off depending on the request_status in the txt-file. To turn the light on or off only the "request_status: " has to be changed and safed while the python script is on going reading it and acting according to the content.

Currently it is sending the a wifi request to the same light-node. So it is nothing special here at the time!
