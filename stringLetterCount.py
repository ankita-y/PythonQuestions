s = "aaabbbccccdddaaaaeeeggdddd"
v = s[0]
count = 0
news = []
for i in s:
    if i != v:
        news.append([v,count])
        v = i
        count = 0
    count += 1
news.append([v,count])
print(news)

# input s = "aaabbbccccdddaaaa"
# output = {'a':3, 'b':3, 'c':4, 'd':3, 'a':4}
# output = [['a', 3], ['b', 3], ['c', 4], ['d', 3], ['a', 4]]
# input s = "aaabbbccccdddaaaaeeeggdddd"
# output = [['a', 3], ['b', 3], ['c', 4], ['d', 3], ['a', 4], ['e', 3], ['g', 2], ['d', 4]]
