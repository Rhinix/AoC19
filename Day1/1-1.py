lines = open("input1-1.txt").readlines()
sum = 0
for line in lines:
    sum += (int(line)//3)-2
print(sum)
