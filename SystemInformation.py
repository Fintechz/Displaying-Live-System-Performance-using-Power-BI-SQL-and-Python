#!/usr/bin/env python
# coding: utf-8

# In[6]:


# import python system and process utilities
import psutil
#import time library
import time
# import ODBC library for python
import pyodbc


# In[7]:


# craete connection using pyodbc library
con = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1C0HFH4;'
                      'Database=System_Information;'
                    'Trusted_Connection=yes;')


# In[ ]:


#Create a SQL cursor using the above connection
cursor = con.cursor()
#create never ending loop
while 1==1:
        # get CPU usage information using python system utility
        cpu_usage = psutil.cpu_percent()
        # memory usage information
        memory_usage = psutil.virtual_memory()[2] 
        # CPU interrupts, which are the signals to the CPU for immediate attention
        cpu_interrupts = psutil.cpu_stats()[1]
        cpu_calls = psutil.cpu_stats()[3]     
        
        memory_used = psutil.virtual_memory()[3]
        momory_free = psutil.virtual_memory()[4]
        
        bytes_sent = psutil.net_io_counters()[0]
        bytes_received = psutil.net_io_counters()[1]
        
        disk_usage = psutil.disk_usage('/')[3]
        
        cursor.execute('insert into performance values (GETDATE(),'
                      + str(cpu_usage)+','
                      + str(memory_usage)+','
                      + str(cpu_interrupts)+','
                      + str(cpu_calls)+','
                       + str(memory_used)+','
                       + str(momory_free)+','
                       + str(bytes_sent)+','
                       + str(bytes_received)+','
                       + str(disk_usage)+')'                       
                      )
        con.commit()
        
time.sleep(1)


# In[ ]:





# In[ ]:




