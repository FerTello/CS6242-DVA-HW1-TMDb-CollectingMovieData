

listMovie = ['12345', '12345', '12345', '12345', '33333', '33333', '98765', '98765']
listSimMovie = ['98765', '55555', '33333', '44444', '55555', '12345', '12345', '77777']

listBoth = ['']*len(listMovie)

for i in range(0, len(listMovie)):
    listBoth[i] = [listMovie[i], listSimMovie[i]]

print(listBoth)
count = 0

delDuplicates = ['']*len(listBoth)
a = 0

# filling in duplicates to be removed in delduplicates[]
for i in range(0, len(listBoth)):
    j = i + 1
    for j in range(i + 1, len(listBoth)):
        if listBoth[i][0] == listBoth[j][1]:
            print("possible duplicate")
            if listBoth[j][0] == listBoth[i][1]:
                print("duplicate found")
                if listBoth[i][0] < listBoth[j][0]:
                    delDuplicates[a] = listBoth[j]
                    a = a + 1
                else:
                    delDuplicates[a] = listBoth[i]
                    a = a + 1

# remove duplicates from listBoth
for i in range(len(delDuplicates)):
    for j in range(len(listBoth)):
        if delDuplicates[i] == listBoth[j]:
            del listBoth[j]
            break


print("listBoth: " + str(listBoth))
print("delDuplicates: " + str(delDuplicates))

