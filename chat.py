
from socket import *
import sys
from thread import *
from os import *
from time import *

s=socket(AF_INET,SOCK_DGRAM)
r=socket(AF_INET,SOCK_DGRAM)

def serv(a,b):
	s.bind((sys.argv[1],1609))
	while 1:
		print s.recvfrom(20)[0]
		system("cat move.wav>/dev/dsp") 

def client(a,b):
	while 1:
		r.sendto(raw_input("gluglu>>"),(sys.argv[2],1609))

start_new_thread(serv,(None,None))

start_new_thread(client,(None,None))

while 1:
	sleep(10)




