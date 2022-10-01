import requests
import re
import os

file='12\\'

if not os.path.exists(file):
  os.mkdir(file)


wy='https://y.music.163.com/m/discover/toplist?id=19723756'

head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36'}

res=requests.get(url=wy,headers=head)

mme=re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>',res.text)              

for nm,tit in mme:    

    mp=f'http://music.163.com/song/media/outer/url?id={nm}.mp3'

    


    music=requests.get(url=mp,headers=head)

    print(nm,tit)  

      
    with open(file+tit+".mp3","wb") as f:

        f.write(music.content)
  
