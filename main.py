from pprint import pprint
import csv
import re

def split_name(element, i):
    n =  element[i].split(' ')
    for name in n:        
        if name != '':
            element[i] = name
            i += 1

def merge_list(contact_list):
    result = dict()
    for elements in contact_list[1::]:
        if elements[0] not in result:
           result[elements[0]] = elements
        else:
            lis = []
            lis = result[elements[0]]
            for index in range(len(elements)):
                if lis[index] == '':
                    lis[index] = elements[index]
    return result

with open("phonebook_raw.csv", encoding='UTF-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  
search_phone_pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
sub_phone_pattern = r'+7(\2)-\3-\4-\5 \6\7'

result = []

for element in contacts_list[1::]:
    rec = []
    split_name(element, 0)
    split_name(element, 1)
    re.sub(search_phone_pattern, sub_phone_pattern, element[5]).strip() 
  
result = merge_list(contacts_list[0::]).values() 

with open("phonebook.csv", "w",encoding='UTF-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(result)