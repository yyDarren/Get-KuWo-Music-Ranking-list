#-*- coding: utf-8 -*-
#DATE:2018/7/6 16:36
import requests,re
url='http://www.kuwo.cn/bang/index'
headers={'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
response=requests.get(url,headers=headers)
html=response.text
# ree=re.compile('<a.*?blank">(.*?)</a')
name=re.findall('<a.*?target="_blank">(.*?)</a>',html,re.S | re.M)
singer=re.findall('content\?name=(.*?)">',html,re.S | re.M)

title=re.search('<title>(.*?)</title>',html,re.S | re.M)
del name[:3]
with open('KuWoYinYue_List.txt','w') as f:
    f.write(title.group(1)+'\n\n\n')
for nameq in name:
    i=name.index(nameq)
    singerq=singer[i]
    # print(nameq+'==='+singerq)
    with open('KuWoYinYue_List.txt','a+') as f:
        f.write(nameq+'==='+singerq+'\n')
