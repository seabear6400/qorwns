rest=[]
for i in range(10):
    add=int(input())
    rest.append(add%42)
rest=set(rest)
print(len(rest))