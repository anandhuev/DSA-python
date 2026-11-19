# n = [5,2,4,2,4,2,1,1,3,4,6]
# m = [112,2,3,1,777,55,89,4]

# hashlist = [0]*11
# for num in n:
#     hashlist[num]+=1
# for x in m:
#     if x<1 or x>10:
#         print(x,"=",0)
#     else:
#         print(x, "=", hashlist[x])

# hashmap= {}
# for num in n:
#     hashmap[num] = hashmap.get(num, 0)+1
# for i in m:
#     if i<1 or i>10:
#         print(i,"=", 0)
#     else:
#         print(i,'=',hashmap[i])

s= 'ayxkjsdldkfjsdalkfjaaskjfasdldfljaskf'
c = ['a', 'd', 'f', 'l', 'k', 'j', 's', 'f']
hl = [0]*26
for i in s:
    asc = ord(i)
    idx = asc - 97
    hl[idx]+=1
for ch in c:
    ascc = ord(ch)
    index = ascc -97
    print(ch, '=', hl[index])
