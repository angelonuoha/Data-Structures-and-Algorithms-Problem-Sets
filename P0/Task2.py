"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
test = [['78130 00821', '98453 94494', '01-09-2016 06:01:12', '186'], ['78298 91466', '(022)28952819', '01-09-2016 06:01:59', '2093'], ['98453 94494', '(022)47410783', '01-09-2016 06:03:51', '1975'], ['93427 40118', '98453 94494', '01-09-2016 06:11:23', '1156']]

my_dict = {}
for call_rec in calls:
    if call_rec[0] not in my_dict.keys():
        my_dict[call_rec[0]] = int(call_rec[3])
    else:
        my_dict[call_rec[0]] += int(call_rec[3])
    if call_rec[1] not in my_dict.keys():
        my_dict[call_rec[1]] = int(call_rec[3])
    else:
        my_dict[call_rec[1]] += int(call_rec[3])

high_val = my_dict.values()[0]
high_key = ""
for key, val in my_dict.items():
    if val > high_val:
        high_val = val
        high_key = key

print("%s spent the longest time, %s seconds, on the phone during September 2016." % (high_key, high_val))

O(n)