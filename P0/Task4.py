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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
texts_set = set()
calls_set = set()
telemarketers_set = set()
for text_rec in texts:
    texts_set.add(text_rec[0])
    texts_set.add(text_rec[1])

for call_rec in calls:
    calls_set.add(call_rec[1])

texts_list = list(texts_set)
calls_list = list(calls_set)
for rec in calls:
    if rec[0] not in texts_list and rec[0] not in calls_list:
        telemarketers_set.add(rec[0])
telemarketers = list(telemarketers_set)
telemarketers.sort()
print("These numbers could be telemarketers:")
for i in telemarketers:
    print(i)

O(n)