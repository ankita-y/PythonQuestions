# Find out the numerology number for the given string

gvn_dict = {1:['A','I','J','Q','Y'],
            2:['B','K','R'],
            3:['C','G','L','S'],
            4:['D','M','T'],
            5:['E','H','N','X'],
            6:['U','V','W'],
            7:['O','Z'],
            8:['F','P']}

usr_str = input().upper()
str_sum = 0

for ch in usr_str:
    for key, value in gvn_dict.items():
        if ch in value:
            str_sum += key

print(str_sum)
print(sum(int(x) for x in str(str_sum)))
# wt = 0
# for i in str(str_sum):
#     wt += int(i)
# print(wt)


