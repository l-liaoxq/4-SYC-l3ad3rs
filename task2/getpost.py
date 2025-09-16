import requests

url = "http://61.147.171.35:62738/"


try:
    response = requests.get(url,params={"a":"1"})
    response = requests.post(url,data={"b":"2"})
    print("响应内容:\n", response.text)

except Exception as c:
    print("请求出错:", str(c))


