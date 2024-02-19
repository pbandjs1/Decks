import requests
import json
import re
import wget
import csv
from pandas import *

url = "https://www.archidekt.com/api/decks/1585124/"
response = requests.get(url)
print(response.status_code)
obj = json.loads(json.dumps(response.json()))

#print(str(obj))
m = re.compile('(?<=}, \'name\': \')((\\w*,?\\s*\'?-?/*)*)')
m1 = re.compile('(?<=\')((\\w*\\s*,*)*)')
deckList = re.findall(m, str(obj))
print(deckList)
# for card in deckList:
#     print("1 " + str(card)[2:len(str(card))-16])

# with open('all-folders.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

data = read_csv('all-folders.csv')
cardStockList = data['Card Name'].tolist()


numberOfMatches = 0
blockedList = []
for card in deckList:
    matchedCards = re.findall(str(card)[2:len(str(card))-16], str(cardStockList))
    i = 0
    if len(matchedCards) > 0:
        re.match(matchedCards[0], str(blockedList))
        if not re.match(matchedCards[0], str(blockedList)):
            if len(matchedCards) > 1:
                blockedList.append(matchedCards[0])
            while i < len(matchedCards):
                numberOfMatches += 1
                i += 1
            print(matchedCards[0])
        else:
            numberOfMatches += 1


print(numberOfMatches)

