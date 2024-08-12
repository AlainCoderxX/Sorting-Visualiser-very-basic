import pickle,random
arr=[]
while len(arr)!=20:
    x=random.choice(range(30))
    if x not in arr:
        arr.append(x)
# print(arr.sort()==set(arr))
print(arr)