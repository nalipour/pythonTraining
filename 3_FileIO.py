filex = open('myfile', 'w')
print(1, 2, 3, 4, file=filex)
filex.write('5 6 7 8')

filex = open('myfile', 'r')
for line in filex:
    print(line)
