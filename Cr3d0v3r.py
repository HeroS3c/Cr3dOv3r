#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
# -*- coding: utf-8 -*-
import os,sys,argparse,requests,time
from getpass import getpass
import mechanicalsoup as ms
from Core import ispwned
from Core.utils import *
from Core.color import *
import json

parser = argparse.ArgumentParser(prog='Cr3d0v3r.py')
parser.add_argument("-p",action="store_true", help="Don't check for leaks or plain text passwords.")
parser.add_argument("-np",action="store_true", help="Don't check for plain text passwords.")
parser.add_argument("-q",action="store_true", help="Quiet mode (no banner).")
args    = parser.parse_args()

os.system('clear')
banner()
#import the list of emails
try:
	filename='email.json'
	with open (filename) as f_obj:
		emaillist= json.load(f_obj)
except:
	print "A problem was occured during opening email.json"
	#start for loop 	
		

def main():
	
		if not args.p:
			status("Checking email: "+email+" in public leaks...")
			ispwned.parse_data(email,args.np)

if __name__ == '__main__':
	
	goodresult= "\n Finished! :D \a"
	badresult=  "\n Oh no, something is wrong! :( \a"
	
try:
	for i in emaillist:
		email=i
		main()	
		time.sleep(0.50)	
	print format(W+goodresult)
	
except ValueError as e:	
	print format(W+badresult,"error: ",e)
	

