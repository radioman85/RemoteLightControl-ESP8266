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

With light_interface.py this file is read and 
