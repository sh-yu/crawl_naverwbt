# -*- coding: utf-8 -*-
#
from __future__ import unicode_literals
import os
import requests
from bs4 import BeautifulSoup


def crawl_naver_webtoon(episode_url):
    html = requests.get(episode_url).text
    soup = BeautifulSoup(html, 'html.parser')

    comic_title = ' '.join(soup.select('.comicinfo h2')[0].text.split())
    ep_title = ' '.join(soup.select('.tit_area h3')[0].text.split())

    for img_tag in soup.select('.wt_viewer img'):
        image_file_url = img_tag['src']
        image_dir_path = os.path.join(os.path.dirname(__file__), comic_title, ep_title)
        image_file_path = os.path.join(image_dir_path, os.path.basename(image_file_url))

        if not os.path.exists(image_dir_path):
            os.makedirs(image_dir_path)

        print(image_file_path)

        headers = {'Referer': episode_url}
        image_file_data = requests.get(image_file_url, headers=headers).content
        open(image_file_path, 'wb').write(image_file_data)

    print(str(n), '화 Completed !')
iD = int(input('작품번호: '))
n = int(input('시작할 화: '))
ne = int(input('완료할 화: '))
while n < ne + 1:
    if __name__ == '__main__':
        wt_url = 'https://comic.naver.com/webtoon/detail.nhn?titleId='
        title_id = str(iD)
        ct_f = '&no='
        wt_no = str(n)
        ep_url = wt_url + title_id + ct_f + wt_no
        crawl_naver_webtoon(episode_url)
        n = n + 1
