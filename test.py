import requests

url = "http://api.img4me.com/?text=Testing&font=arial&fcolor=000000&size=10&bcolor=FFFFFF&type=png"
response = requests.request("GET", url)

print(response.text)
