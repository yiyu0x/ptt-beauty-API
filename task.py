from datetime import datetime 
from get_image import getUrl
import time 
import os

# 60*30 , every 30 minutes will update
frequency = 1800
url_list_size = 5000

def timedTask(): 
	while True:
		file = open('url_list.txt')
		print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		print('start to get image ...')
		getUrl()
		lines = len(file.readlines())
		print('done, url_list.txt have',lines,'lines.')
		if lines > url_list_size :
			del_lines = str(lines - url_list_size)
			os.system('sed -i \'1,'+del_lines+'d\' url_list.txt')
		time.sleep(frequency)




