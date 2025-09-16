import requests

url = "     ababababab"


data ={
    "imoau": "sb",
    "xt": "大帅b"
}

headers = {
    "Referer": "https://www.xidian.edu.cn/",  
    "Cookie": "user=admin",  
    "User-Agent": "MoeBrowser/1.0",  
    "X-Forwarded-For": "127.0.0.1"  
}

try:
    response = requests.post(
        url=url,
        data=data,
        headers=headers,
        timeout=10
    )
    print("响应内容:\n", response.text)

except Exception as c:
    print("请求出错:", str(c))
