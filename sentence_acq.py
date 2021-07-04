import requests
from lxml import html
import re

def getContent():
    url = 'https://language.chinadaily.com.cn/trans_collect/'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    html_data = resp.text
    selector = html.fromstring(html_data)
    ul_list = selector.xpath('//div[@class="content_left"]/div[@class="gy_box"]')


    html_text = html.tostring(ul_list[0], encoding='utf-8').decode('utf-8')
    title = re.findall(r">(.+?)</a>", html_text)
    urls = re.findall(r"href=\"(.+?)\">", html_text)
    url = 'https:' + urls[0]

    all = []
    all.append(title[1])
    all.append(title[2])
    all.append(url)
        
    return all

if __name__ == '__main__':
    getContent()

