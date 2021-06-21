# Swap the key and value in Dictionary
payload = {'elevan':[11],'twelve':[12,13,14],'thirteen':[15,16],'four':[15,16]}
new_payload = {}
for key,val in payload.items():
# As Dictionary contains list of value it will give unhashable error for 'list' so for it, 
# convert the list into tuple and then take it as key in dictionary. List can't be a key in dictionary 
    val = tuple(val)
    if val not in new_payload:
        new_payload[val] = [key]
    else:
        new_payload[val].append(key)
        
print(new_payload)

# Output
# {(11,): ['elevan'], (12, 13, 14): ['twelve'], (15, 16): ['thirteen', 'four']}
# {(11,): 'elevan', (12, 13, 14): 'twelve', (15, 16): 'thirteen'}

payload = {'a':97,'b':98,'c':99,'d':100}
newpayload = {val:key for key,val in payload.items()}
print(newpayload)

# Output
# {97: 'a', 98: 'b', 99: 'c', 100: 'd'}
