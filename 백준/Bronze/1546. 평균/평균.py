test=int(input())
test_count=list(map(int,input().split()))
max_score = max(test_count)

fake_list=[]
for i in test_count:
  fake_list.append(i/max_score*100)
avg=sum(fake_list)/test
print(avg)