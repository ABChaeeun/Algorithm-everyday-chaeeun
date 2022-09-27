title = list(input())

for i in range(len(title)):
    if title[i].islower():
        title[i] = title[i].upper()
        
print(''.join(title))