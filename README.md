# ptt-beauty-API
💻 PTT表特版自動回傳圖片網址API 🤖️

A api can give you beauty girl photo from ptt (A popular forum in Taiwan)

## demo


![shot](https://i.imgur.com/qvA4n6Z.png)


## api usage

### random give a image url
> http://ip:5001

### random give many images url
> http://ip:5001/times/<number\>
 
(number range just support 1 ~ 100)

## build

### build service on your server 

clone repo  
> git clone https://github.com/yiyu0x/ptt-beauty-API.git && cd ptt-beauty-API

install packages
> pip3 install -r requirements.txt

run it / 執行
> python3 app.py

### build with docker

> docker run -d -p 5001:5487 yiyu0x/ptt-beauty-api:2.1


### build with compose
(docker-compose.yml 第 22 行記得改為 server ip)
> docker-compose up --scale api=3 -d
