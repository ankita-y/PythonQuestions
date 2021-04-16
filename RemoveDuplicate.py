sentence = input().split()
new_sent = []
for i in sentence:
    if i not in new_sent:
        new_sent.append(i)
print(" ".join(c for c in new_sent))
