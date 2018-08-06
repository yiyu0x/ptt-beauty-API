# 開啟檔案
# fp = open("image.json", "a")
 
# # 寫入 This is a testing! 到檔案
# fp.write("This is a testing!")
 
# # 關閉檔案
# fp.close()

from bs4 import BeautifulSoup
import urllib3
import urllib3.contrib.pyopenssl
import random
import re
http = urllib3.PoolManager()
urllib3.disable_warnings()


post_list = []
url_list = []

def getUrl():
    # https://www.ptt.cc/bbs/Beauty/index2600.html
    page_num = random.randint(2000,2600)
    urllib3.contrib.pyopenssl.inject_into_urllib3()
    url = "https://www.ptt.cc/bbs/Beauty/index"+str(page_num)+'.html'
    response = http.request('GET', url)
    soup = BeautifulSoup(response.data,'html.parser')

    f = open("url_list.txt", "a")
    
    for a_tag in soup.select('a'):
        # format
        # <a href="/bbs/Beauty/M.1471237548.A.EAB.html">[正妹] 體育主播</a>
        match = re.search(r'<a href="/bbs/Beauty/M(.*?)">\[正妹\]',str(a_tag))
        if match:
            article_url = 'https://www.ptt.cc/bbs/Beauty/M'+match.group(1)
            url_list.append(article_url)
    
    for url in url_list:
        response = http.request('GET', url)
        soup = BeautifulSoup(response.data,'html.parser')
        
        for a_tag in soup.select('a'):
            # format
            # <a href="http://i.imgur.com/e5UD40k.jpg" rel="nofollow" target="_blank">http://i.imgur.com/e5UD40k.jpg</a>
            # print(a_tag)
            match = re.search(r'<a href="http(s)?://(i\.)?imgur\.com/(.*?)\.jpg"',str(a_tag))
            if match:
                image_url = 'https://imgur.com/'+match.group(3)+'.jpg'
                f.write(image_url+'\n')
        

getUrl()
    
# return final_url