marks = []

# for i in range(5):
#     fruit  = input("Enter 5 fruits name ")
#     fruits.append(fruit)


# for fruit in fruits:
#     print(fruit)

# for i in range(5):
#     mark = int(input("Enter marks of 5 students only:{} ".format(i+1)))
#     marks.append(mark)
    

# sum=0
# for i in marks:
#     sum += i
# print(sum)

# zeros = (0,0,0,0,0,000,0)

# count=0

# for i in zeros:
#     if(i==0):
#         count+=1
# print(count)\
    
    
# num = []
# for i in range(5):
#     no = int(input("Enter num{}:".format(i+1)))
#     num.append(no)
    

# print(max(num))

# English = 0
# Maths = 0
# Science  = 0

# English = int(input("Enter marks of english "))
# Maths = int(input("Enter marks of Maths "))
# Science = int(input("Enter marks of Science "))

# percent = English+Maths+Science/300*100

# if(English/100*100 >= 33 and Maths/100*100 >= 33 and Science/100*100>=33):
#     print("Pass")
# else:
#     print("Failed")

# poem  = '''In the quiet of the night,
# Stars above so softly gleam,
# Moonlight casts a silver light,
# On the edges of a dream.

# Silent whispers on the breeze,
# Through the leaves that gently sway,
# In the stillness, find your peace,
# As the night turns into day.

# '''

# username = input("Enter username: ")

# count=0
# for i in username:
#     count+=1

# if(count<10):
#     print("Invalid Username")
# else:
#     print("Valid Username")

# name_list = ['Alex','Robin','Stuart','jimmy','Leena']

# name  = input("Enter Name: ")

# for i in name_list:
#     if(name_list.__contains__(name)):
#         print("Present")
#         break
#     else:
#         print("Not present")
#         break

Marks = int(input("Enter your marks "))

if(Marks>=90):
    print("A+")
elif(Marks>=80 and Marks<90):
    print("A")
elif(Marks >= 70  and Marks < 80):
    print("B+")
elif(Marks >= 60 and Marks < 70):
    print("B")