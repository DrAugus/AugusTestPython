# coding:utf-8
# 引入requests包和正则表达式包re
import requests
import re


# 自定义下载页面函数
def load_page(url):
    response = requests.get(url)
    print(response)
    data = response.content
    return data


# 自定义保存页面图片函数
def get_image(html):
    regx = r'http://[\S]*jpg'  # 定义图片正则表达式
    pattern = re.compile(regx)  # 编译表达式构造匹配模式
    get_images = re.findall(pattern, repr(html))  # 在页面中匹配图片链接

    num = 1
    # 遍历匹配成功的链接
    for img in get_images:
        image = load_page(img)  # 根据图片链接，下载图片链接
        if image == "":
            continue
        # 将下载的图片保存到对应的文件夹中
        with open('./spider_picture/%s.jpg' % num, 'wb') as fb:
            fb.write(image)
            print("正在下载第%s张图片" % num)
            num = num + 1
        print("only first one")
        break
    print("下载完成！")

if __name__ == '__main__':
    # 定义爬取页面的链接
    url = 'https://cn.bing.com/images/search?q=%E9%83%AD%E9%87%87%E6%B4%81&qs=IM&form=QBILPG&sp=1&pq=gcj&sc=8-3&cvid=A98D1596ACC3462C838BB4A67DC0FCA0&first=1&tsc=ImageBasicHover'
    # 调用load_page函数，下载页面内容
    html = load_page(url)
    # 在页面中，匹配图片链接，并将图片下载下来，保存到对应文件夹
    get_image(html)

