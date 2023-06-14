# Check string is valid or not for paranthesis
# s = 'Qwe{s}{aqwe{ds}a}'
s =  'Qwe{s}{aqwe}{ds}a'
# s = 'Qwe{s}{aqwe{dsa}'
# s = 'Qwe{s}{aq}w}e{ds}a}{{'

lcount = 0
rcount = 0
flag = 1

for i in range(len(s)):
    
    if s[i] == '{':
        lcount += 1
    if s[i] == '}':
        rcount += 1
        
        if rcount>lcount:
            flag = 1
        else: 
            lcount,rcount = 0,0
            flag = 0
    
if flag == 1:
    print('invalid')
else:
    print('valid')
