S = list(input())
alphabet = []

for i in range(26):
    alphabet.append(chr(i+97))

x = set(S)

for i in alphabet:
    if i not in x:
        print(i)
        exit()

print('None')