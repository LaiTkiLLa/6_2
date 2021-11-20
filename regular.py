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

main()
