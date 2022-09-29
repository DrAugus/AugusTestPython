import requests
from lxml import etree
from requests.exceptions import ConnectionError


def get_one_page(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/89.0.4389.114 Safari/537.36 "
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response
        return None
    except ConnectionError:
        return None


def main(num):
    url = 'https://genshin.hoyoverse.com/en/news/detail/' + str(num)
    print(url)
    resp = get_one_page(url)
    # print(resp.text)
    # 将结果集的文本转化为树的结构
    tree = etree.HTML(resp.text)
    print(tree)
    print(etree.tostring(tree))
    path = '//*[@id="frame"]/div[3]/div/div[2]/div/div[2]/div[3]/p[2]'
    ele = tree.xpath(path)
    print(ele)



if __name__ == '__main__':
    main(24200)
