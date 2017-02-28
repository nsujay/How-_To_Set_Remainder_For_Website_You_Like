# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 08:09:05 2017
read the detalis.txt file for explanation
read the applications.txt file for applications of this program
"""

import time
import webbrowser

remainder_time = raw_input(" Enter the time to set remainder as H:M:S ")
site_addr = raw_input ("Enter the website address ")
present_time = time.strftime("%I:%M:%S")
print("We will remaind you.... carry on your work") 


def check_time():
     present_time=time.strftime("%I:%M:%S")
     return present_time
  
while(remainder_time != present_time):  
      present_time=check_time()
      
        
print("Its Over Hurry Up")
webbrowser.open(site_addr) 
 

