from datetime import datetime 
from get_image import getUrl
import time 

def timedTask(): 
	while True: 
		print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		getUrl()
		# 60*30 , every 30 minutes will update
		time.sleep(1800)




