# 爬取豆瓣
import requests
from bs4 import BeautifulSoup as bs
from time import sleep


def get_url_name(my_url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                 'Chrome/84.0.4147.125 Safari/537.36 '
    header = {'user-agent': user_agent}

    response = requests.get(my_url, headers=header)

    # print(response.text)

    bs_info = bs(response.text, 'html.parser')
    # print(bs_info.find_all('div', attrs={'class': 'pl2'})[0])

    for tags in bs_info.find_all('div', attrs={'class': 'pl2'}):
        # 获取a标签
        # a_tag = tags.contents[1]
        # print(a_tag)
        for a_tag in tags.find_all('a'):
            # 获取所有链接
            print(a_tag.get('href'))
            # 获取图书名字
            print(a_tag.get('title'))


urls = tuple(f'https://book.douban.com/top250?start={page * 25}' for page in range(10))

if __name__ == '__main__':
    for page in urls:
        get_url_name(page)
        sleep(5)
