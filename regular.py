from pprint import pprint
import csv
import re

PHONE_SEARCH = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_GROUPS = r'+7(\2)-\3-\4-\5 \6\7'

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=";")
  contacts_list = list(rows)
# pprint(contacts_list)

def main():
  new_list = list()
  for item in contacts_list:
    name = ' '.join(item[0:2]).split(' ')
    print(name)
    
  #я понимаю как работает код и что дальше нужно работать просто с индексами, после чего сделать аппенд, но я не понимаю почему тут код ведет себя не так как мне нужно)
# джойню строки и разбиваю на списки, каждое слово - список, но во всех строках списки из нескольких слов, в 1 строке вообще вся строка - один список
# из за этого не получается работать с ним как с индексом, если индекс больше 0, то сразу вылезает ошибка

main()
