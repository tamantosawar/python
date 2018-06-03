import time
import os
x=''' 
	Press 1: to Show current Time 
	Press 2: to Reboot OS
        Press 3: to create user in your current os 
        Press 4: to search something on google'''
print x
choice = int(raw_input())
if choice ==1 :
	print "Showing current time :  "
	print time.ctime().split()[3]
elif choice ==2:
	print 'rebooting OS'
	os.system('reboot')
elif choice ==3 :
	print 'search on google'
else: 
	print 'no chance'
	

