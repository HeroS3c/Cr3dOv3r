# -*- encoding: utf-8 -*-
#Written by: Karim shoair - D4Vinci ( Cr3dOv3r )
import sys,os
from . import updater
from .websites import *
from .color import *

def getinput(text):
	# Return the suitable input type according to python version
	
	if ver=="3":
		return input(text)
	else:
		return raw_input(text)

def banner():
	banner = open(os.path.join("Data","banners.txt")).read()
	os.system('clear')
	banner_to_print = G + banner.format(Name=R+"Cr3d0v3r By "+Bold+B+"D4Vinci - Edited by HeroS3c" + G,
									Description=C+"Know the dangers of email credentials reuse attacks."+G,
									MassiveVersion=R+"Cr3d0v3r Mass:"+G+ " The Cr3d0v3r Version for check an entire list of emails"+B+" ("+C+"Created by"+B+" HeroS3c)"+G) + end
	print(banner_to_print)

all_websites =list(websites.keys()) + list(custom_websites.keys()) + list(req_websites.keys())
