import requests
import lxml.etree
import pandas as pd

url = 'https://book.douban.com/subject/35067595/?icn=index-latestbook-subject'

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'

header = {'user-agent': user_agent}

response = requests.get(url, headers=header)
selector = lxml.etree.HTML(response.text)

name = selector.xpath('//*[@id="wrapper"]/h1/span/text()')
print(name)

my_list = [str(name), 'rex', '4.5']
columns_name = ['one']


book1 = pd.DataFrame(columns=columns_name, data=my_list)
book1.to_csv('./book1.csv', encoding='gbk')
