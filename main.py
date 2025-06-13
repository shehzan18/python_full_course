# def add(a,b):
#     a+=1
#     print(x)
#     print(z)
#     print(a)
#     return a+b
# x , y = 1 , 1
# z = 10
# print(add(x,y))
# z = 10
# print(x) 

def add(a , l = []):
    l.append(a)
    return l

l1 = [1,2,3]
add(4 , l1)
print(l1)

print(add(22))
print(add(33))
print(add(44))

add(5 , l1)
print(l1)

print(add(55))
