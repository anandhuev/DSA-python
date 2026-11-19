#print x n times
# def func(x,n):
#     if n==0:
#         return
#     print(x)
#     func(x,n-1)

# func(15,4)


#1 to N using head
# def func(i,n):
#     if i>n:
#         return
#     print(i)
#     func(i+1,n)
# func(2,7)

#n to 1 tail
# def func(i,n):
#     if i>n:
#         return
#     func(i+1,n)
#     print(i)
# func(1,4)

#n to 1 head
# def func(n):
#     if n==0:
#         return
#     print(n)
#     func(n-1)
# func(7)


#1 to n tail
def func(n):
    if n == 0:
        return
    func(n-1)
    print(n)
func(8)