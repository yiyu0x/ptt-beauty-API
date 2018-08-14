# ptt-beauty-API
💻 PTT表特版自動撈圖API 🤖️

A api can give you beauty girl photo from ptt (A popular forum in Taiwan)

## demo

[http://178.128.61.189:5000/](http://178.128.61.189:5000/)

This demo site may not available at any time .

![shot](https://i.imgur.com/qvA4n6Z.png)


## api usage

### random give a image url
> http://ip:5000

### random give many images url
> http://ip:5000/times/<number\>
 
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

> docker run -d -p 5000:5487 yiyu0x/ptt-beauty-api:2.0
