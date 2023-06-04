student=[]
absent=[]
for i in range(28):
    Attend=int(input())
    student.append(Attend)
for i in range(1,31):
    if i not in student:
        absent.append(i)
print(min(absent))
print(max(absent))