#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#@title Time Execution 
import time 
from IPython.display import clear_output 
 
def zero_to_infinity(): 
    i = 0 
    while True: 
        yield i 
        i += 1 
        time.sleep(1) 
 
start = time.time() 
for x in zero_to_infinity(): 
    clear_output(wait=True) 
    end = time.time() 
    temp = end-start 
    hours = temp//3600 
    temp = temp - 3600*hours 
    minutes = temp//60 
    seconds = temp - 60*minutes 
    print("") 
    print('%s %d:%d:%d' %("Time execution : ",hours,minutes,seconds)) 
    print("")

