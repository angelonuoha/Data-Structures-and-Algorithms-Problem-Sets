"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def checkIfBangladore(phone_num):
  if phone_num[0] == '(' and phone_num[1] == '0' and phone_num[2] == '8' and phone_num[3] == '0' and phone_num[4] == ')':
    return True
  else:
    return False

def getAreaCode(receiver_num):
  if receiver_num[0] == '(':
    return receiver_num[1] + receiver_num[2] + receiver_num[3]
  else:
    return receiver_num[0] + receiver_num[1] + receiver_num[2] + receiver_num[3]

my_set = set()
my_array = []
for rec in calls:
  if checkIfBangladore(rec[0]):
    area_code = getAreaCode(rec[1])
    my_set.add(area_code)
    my_array.append(area_code)
answer = list(my_set)
answer.sort()
print("The numbers called by people in Bangalore have codes:")
for i in answer:
  print(i)

count = 0
for i in my_array:
  if i == '080':
    count += 1
percentage = float((float(count) / len(my_array)) * 100)
print("{:0.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore." .format(percentage))

O(n)