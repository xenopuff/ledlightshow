__author__ = 'leahscott'
import serial
import urllib2
port = serial.Serial("/dev/cu.usbmodem1411",9600,timeout=2)
input = port.readline()
led = 13
print(input)
port.write("Hello")
port.close
response = urllib2.urlopen("http://store.apple.com/uk/mac")
html = response.read()
print(html[:350])
