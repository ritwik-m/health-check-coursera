#!/usr/bin/env/python3
import os
import shutil
import sys

def check_reboot():
    """ Returns True if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk,min_absoloute,min_percent):
	"""Returns True if there isn't enough disk space, False otherwise"""
	du = shutil.disk_isage(disk)
	#Calculate percentage of free space
	perecnt_free =100*du.free/du.total
	#Calculate Free bytes
	gigabytes_free = du.free/2**30
	if perecnt_free<min_percent or gigabytes_free< min_absoloute:
		return True
	return False


def main():
	if check_reboot():
		print("Pending Reboot.")
		sys.exit(1)
	if check_disk_full("/",2,10):
		print("Disk full.")
		sys.exit(1) 
		
    print("Everything ok.")
    sys.exit(0)

main()