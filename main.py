f = open("file.txt", "r")
searchlines = f.readlines()
f.close()
for i, line in enumerate(searchlines):
    if "searchphrase" in line: 
        for l in searchlines[i:i+3]: print l,
        print
