import requests

newproxy = requests.get(url = 'http://192.168.31.192:5555/random').text

print('获取新的IP：'+ newproxy)