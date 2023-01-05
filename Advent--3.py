#%% Part 1
file = open("advent3data.txt")
data = file.readlines()
file.close()
data = [x[:-1] for x in data]
firsthalves = []
secondhalves = []
for i in range(len(data)):
    firsthalves.append(data[i][:int(len(data[i])/2)])
    secondhalves.append(data[i][int(len(data[i])/2):])
commonletters = []
for j in range(len(data)):
    commonletters.append(sorted(set.intersection(set(firsthalves[j]), set(secondhalves[j]))))

alphabetkey=[]
for n in range(97,123):
    alphabetkey.append(chr(n))
for n in range(65,91):
    alphabetkey.append(chr(n))

priorities = []
for k in range(len(data)):
    let = commonletters[k][0]
    pri = int(alphabetkey.index(let)) + 1
    priorities.append(pri)
    
print(sum(priorities))


#%% Part 2
file = open("advent3data.txt")
data = file.readlines()
file.close()
data = [x[:-1] for x in data]
data = [data[x:x+3] for x in range(0, len(data), 3)]
commonletters = []
for j in range(len(data)):
    let = sorted(set.intersection(set(data[j][0]), set(data[j][1]), set(data[j][2])))
    if let is not '':
        commonletters.append(str(let))

alphabetkey=[]
for n in range(97,123):
    alphabetkey.append(chr(n))
for n in range(65,91):
    alphabetkey.append(chr(n))

priorities = []
for k in range(len(data)):
    let = commonletters[k][2]
    pri = int(alphabetkey.index(let)) + 1
    priorities.append(pri)
print(sum(priorities))
