import openpyxl as xl
import json
import random

wb = xl.load_workbook('N4_Kanji_List.xlsx')
sheet = wb['Sheet 1']


def get5Kanji():
    rando = random.sample(range(2, 332), 5)
    data = []
    for rand in rando:
        data.append({
            "kanji": sheet.cell(rand, 3).value,
            "hiragana": sheet.cell(rand, 2).value,
            "word": sheet.cell(rand, 1).value
        })

    return data


def getXKanji(quantity):
    spl_word = ' '
    num = int(quantity.partition(spl_word)[2])
    rando = random.sample(range(2, 332), num)
    data = []
    for rand in rando:
        data.append({
            "kanji": sheet.cell(rand, 3).value,
            "hiragana": sheet.cell(rand, 2).value,
            "word": sheet.cell(rand, 1).value
        })
    return data,num


if __name__ == "__main__":
    get5Kanji()