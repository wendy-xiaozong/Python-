from urllib import request, parse, error
import re
# 将从网页上复制下来的cookie转化成dic格式
import gzip
from http import cookiejar
# 获取Cookie对象
cookie = cookiejar.CookieJar()
# 返回一个Cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 获取一个带Cookie的请求管理器
opener = request.build_opener(cookie_handler)

# 定义url和需要提交的数据
url = "http://dict.youdao.com/w/{}/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'}
print("输入exit时退出程序")
word = input("请输入需要翻译的词语")
# 提交数据  
try:
    while( word != 'exit'):
        req = request.Request(url.format(word), headers = headers, method = 'GET')
        # 获取网页数据
        res = opener.open(req)
        data = res.read().decode("utf-8")
        explain = '<div class="trans-container">\s.*?\s   <ul>\s     <li>(.*?)</li>'
        # 使用正则表达式匹配结果
        print(re.compile(explain).findall(data)[0])
        word = input("请输入需要翻译的词语")
except Exception as e:
    print(e)

