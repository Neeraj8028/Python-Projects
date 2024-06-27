# def polysm(p1,p2):
#     return p1*p2
# -------------------------------------- Polymorphism
# print(polysm('W',2))


# def multiple(radius,pi):
#     area =  pi*radius*radius
#     circum = 2*pi*radius
    
#     return(area,circum)

# print(multiple(4,3.14))


# def greet(name="user"):
#     print("Hello",name)
    
# greet("Neeraj")



# cube  = lambda x: x**3
# print(cube(3))


# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2,3,4,5))

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
        
        
# print(even_generator(11))
for num in even_generator(10):
    print(num)