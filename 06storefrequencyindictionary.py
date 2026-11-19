#method 1
# num = [1,1,1,4,5,2,3,4,5,2,4,7,8,3,4,2,7]
# fmap = dict()
# for i in range(0,len(num)):
#     if num[i] in fmap:
#         fmap[num[i]]+=1
#     else:
#         fmap[num[i]]=1
# print(fmap[7])


#method 2(hashing)
num = [1,1,1,4,5,2,3,4,5,2,4,7,8,3,4,2,7]
hashmap ={}
for i in range(0,len(num)):
    hashmap[num[i]] = hashmap.get(num[i],0)+1
print(hashmap[8])
