def strcount(strv):
    data = ''
    x = 1
    for i in range(len(strv)):
        try:
            if strv[i] == strv[i+1]: x += 1
            else:
                data += strv[i]+str(x)
                x = 1
        except IndexError:
            data += strv[i]+str(x)
    print(data)
strcount('a')
# a1
strcount('aabbb')
# a2b3
strcount('aabbbaa')
# a2b3a2
strcount('aabbc')
# a2b2c1
strcount('aa')
# a2
