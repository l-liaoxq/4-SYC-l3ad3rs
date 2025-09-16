import requests

url = "https://www.baidu.com"

try:
    response = requests.get(url)
    response.raise_for_status()  
    

    print("百度首页：")
    print(response.text)

except requests.exceptions.RequestException as c:
    print(f"请求失败：{c}")