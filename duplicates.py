
listMovie = ['12345', '12345', '12345', '12345', '33333', '33333', '98765', '98765']
listSimMovie = ['98765', '55555', '33333', '44444', '55555', '12345', '12345', '77777']

listBoth = ['']*len(listMovie)

for i in range(0, len(listMovie)):
    listBoth[i] = [listMovie[i], listSimMovie[i]]

print(listBoth)
count = 0

delDuplicates = []

# filling in duplicates to be removed in delDuplicates[]
for i in range(0, len(listBoth)):
    j = i + 1
    for j in range(i + 1, len(listBoth)):
        if listBoth[i][0] == listBoth[j][1]:
            print("possible duplicate")
            if listBoth[j][0] == listBoth[i][1]:
                print("duplicate found")
                if listBoth[i][0] < listBoth[j][0]:
                    delDuplicates.append(listBoth[j])
                else:
                    delDuplicates.append(listBoth[i])

# remove duplicates from listBoth[]
for i in range(len(delDuplicates)):
    for j in range(len(listBoth)):
        if delDuplicates[i] == listBoth[j]:
            del listBoth[j]
            break


print("listBoth: " + str(listBoth))
print("delDuplicates: " + str(delDuplicates))


a = 4
b = 5
dumList = []
dumList.append(['1', '1'])
dumList.append([str(a), str(b)])
dumList.append(['3', '3'])
dumList.append(['4', '4'])


print("dumList: " + str(dumList))
