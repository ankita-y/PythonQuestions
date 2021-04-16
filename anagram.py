#Check the given string is Anagram or not?
str1 = input()
str2 = input()

def anagram(str1,str2):
    str1 = ''.join(sorted(str1.replace(" ","").lower()))
    str2 = ''.join(sorted(str2.replace(" ","").lower()))
    if len(str1) != len(str2):
        return False
    else:
        if str(str1) == str(str2):
            return True
        else:
            return False

if anagram(str1,str2):
    print("Both the strings are anagram of each other.")
else:
    print("The given strings are not anagram.")


#Input
# Tom Marvolo Riddle
# I am Lord Voldemort

#act
#cat
# To replace space from string without using in built function
# str = "I am lord Voltemort"
# str1 ="".join([c for c in str if c != " "])
# print(str1)

