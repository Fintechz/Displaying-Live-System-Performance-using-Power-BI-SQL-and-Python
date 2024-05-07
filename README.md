# Displaying-Live-System-Performance-using-Power-BI-SQL-and-Python
Display system performance information using Power BI, SQL, and Python in a Power BI dashboard in real time like a task manager.

Here we are using major 3 data science applications together.
1.	Using python, to read system performance information and insert it into Microsoft SQL server database.
2.	Using Power BI, read the information from the Microsoft SQL server and display it on the dashboard in real-time. 
Steps:
1.	Creating Microsoft SQL database – name: system information
1.a. Create a table – “Performance”
Columns
Time	datetime	
cpu_usage	numeric(5, 2)	
memory_usage	numeric(5, 2)	
cpu_interrupts	numeric(18, 0)
cpu_calls	numeric(18, 0)
memory_used	numeric(18, 0)
memory_free	numeric(18, 0)
bytes_sent	numeric(18, 0)
bytes_received	numeric(18, 0)
disk_usage	numeric(5, 2)
2.	Using Python to get the system performance.
3.	Connect Power BI with the SQL server
4.	In Power BI creating measurements for the latest values
5.	Creating power BI live dashboards 

Sample Python and power BI files are uploaded.

