# Radiation Detector
# By Casey Halverson, copyright 2011.  
# MIT License (see README)
#  
# This code was intended to be ran on Mac OSX and has been tested with Lion 
# and Snow Leapord.  Modification might be required for your particular platform
#
# using a sparkfun usb geiger counter as found here: http://www.sparkfun.com/products/9848
# Be sure to install PySerial and curl

import time
import sys
import serial
import os

# configuration settings

url = "https://example.com/data/collection/url.php"            # url to post your data to
logfile = "/var/log/radlog.txt"                                # location to save log data
serial_port = "/dev/tty.usbserial-A800cBcP"                    # the serial port the counter shows up as (do a ls /dev/*usbserial* to determine what yours is)
magic_key = "thisismyspecialkey"                               # an API key to avoid just anybody from posting to your url

f = open(logfile,"a")

ser = serial.Serial(serial_port,9600,timeout=1)

one = 0

while 1==1:
  stamp = int(time.time())
  stamp == round(stamp,0)
  stamp = stamp + 60
  count = 0
  while 1==1:
      ct = int(time.time())
      ct == round(ct,0)
      if ct > stamp:  break
      bit = ser.read(1)
      if bit != "":
          count = count + 1
  at = str(time.asctime())
  t = str(time.time())
  f.write("["+at+"."+t+"] "+str(count)+"\n")
  print "["+at+"."+t+"] Count "+str(count) 
  os.system("/usr/bin/curl --data rad=\""+str(count)+"\" --data epoc=\""+str(t)+"\" --data key=\""+str(key)+"\" "+str(url)+" &")
 

