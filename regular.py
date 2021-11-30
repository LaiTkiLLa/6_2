
from pprint import pprint
import csv
import re

PHONE_SEARCH = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
PHONE_GROUPS = r'+7(\2)-\3-\4-\5 \6\7'



with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

def name(contacts_list: list):
    new_contact_book = list()
    for text in contacts_list:
        text_join = (',').join(text)
        full_name_split = re.split(",| ", text_join)
        numbers_sub = re.sub(PHONE_SEARCH,PHONE_GROUPS,text_join)
        number_split = numbers_sub.split(',')
        contact_book = [full_name_split[0], full_name_split[1], full_name_split[2], text[3], text[4], number_split[5], text[6]]
        new_contact_book.append(contact_book)
    return union(new_contact_book)


def union(contacts_list: list):
    for contact in contacts_list:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in contacts_list:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]

    result_list = list()
    for i in contacts_list:
        if i not in result_list:
            result_list.append(i)

    print(result_list)


with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(name(contacts_list))
