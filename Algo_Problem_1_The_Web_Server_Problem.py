file = open('input.txt', 'r')
l = []
n = file.readline()
for x in file.readlines():
    l.append(tuple(x.split()))
    
# y=[]
# u=[]
# o=[]
sorted_by_second = sorted(l, key=lambda tup: tup[1], reverse=True)
for x in l:
    print(x)
#     for v in range(0,3):
#         y.append(int(x[0]))
#         u.append(int(x[1])/20)
#         o.append(int(x[2])/5)
        
# y.sort()
# u.sort(y)
# o.sort()
file2 = open('output.txt', 'w')
for i in l:
    i = list(i)
    file2.write(str(i[0])+","+str(i[1])+","+str(i[2])+"\n")
    # file2.write(str(str(y[i])+","+str(int(u[i]*20)))+","+str(int(o[i]*5))+"\n")
