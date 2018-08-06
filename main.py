from datetime import datetime 
import time 

def timedTask(): 
	while True: 
		print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		time.sleep(3)

if __name__ == '__main__': 
	timedTask()


