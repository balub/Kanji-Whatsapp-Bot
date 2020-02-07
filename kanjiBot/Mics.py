import requests

url = "http://api.img4me.com/?text=Testing&font=arial&fcolor=000000&size=10&bcolor=FFFFFF&type=png"
response = requests.request("GET", url)

print(response.text)

def KanjiTestAnswerImageUrl(date,meaningList,hiraganaList):
    url = f"http://api.img4me.com/?text=The%20Answers%20of%20the%20Kanji%20for%20{date}%0D%0A{meaningList[0]}%20{hiraganaList[0]}%0D%0A{meaningList[1]}%20{hiraganaList[1]}%0D%0A{meaningList[2]}%20{hiraganaList[2]}%0D%0A{meaningList[3]}%20{hiraganaList[3]}%0D%0A{meaningList[4]}%20{hiraganaList[4]}%0D%0A&font=arial&fcolor=000000&size=10&bcolor=FFFFFF&type=png"
    response = requests.request("GET", url)
    print(response.text)

    return response.text