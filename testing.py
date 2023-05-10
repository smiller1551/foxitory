from datetime import datetime, timedelta
from time import sleep

first_time = datetime.now()
print(first_time)

sleep(20)

second_time = datetime.now()
print(second_time)

difference = second_time - first_time
print(difference)

if difference < timedelta(seconds=2):
    
    print("move fox")
    
else: 
    
    print("stay")
    

