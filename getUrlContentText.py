import requests
from multiprocessing import Pool

from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError
import re
import json


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response
        return None
    except ConnectionError:
        return None


def get_class(soup, class_str):
    for cc in soup.select(class_str):
        print(cc)


def get_id(soup):
    e = soup('#title')
    print(e)


def unicode_gb2312(data):
    data = str(data, 'gb2312')
    print(data)


def parse_one_page(index, html):
    # print('=========')
    html = html.text.encode('iso-8859-1').decode('gbk')

    soup = BeautifulSoup(html, 'html.parser')

    str_all = ''.join([str(x.text) for x in soup.select('.STYLE4')])
    print(str_all)

    new_res = re.findall(r"译文](.+?)\[注释", str_all)
    # print(len(new_res))

    ins = ""
    if len(new_res) != 1:
        ins = "error"
    else:
        ins = new_res[0]

    write_to_file(str(index) + ": " + ins)

    # header = soup.select('p')

    # print(header)
    # print(header[0])  # 去除中括号保留标签和文本
    # print(header[0].text)  # 去除标签保留文本


def write_to_file(content):
    with open('spider/text/result.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()


def main(num):
    url = 'https://www.daodejing.org/' + str(num) + '.html'
    print(url)
    html = get_one_page(url)
    parse_one_page(num, html)


if __name__ == '__main__':
    for i in range(1, 82):
        main(i)
