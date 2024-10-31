# # Exercise - 1
# num1 = input("Enter your 1st number: ")
# num2 = input('Enter your 2nd number: ')

# num1 = int(num1)
# num2 = int(num2)

# print("Addition: ", num1+num2)
# print("Substruction: ", num1-num2)
# print("Multiplication: ", num1*num2)
# print("Division: ", num1/num2)
# print("Modulus: ", num1%num2)


# # Excersise - 2
# age = int(input("Enter your age: "))

# if age >= 18:
#     print("You are an adult")
# else:
#     print("You are not adult")

### ১. For Loop ব্যবহার করে ১ থেকে ১০ পর্যন্ত সংখ্যা প্রিন্ট
# for _ in range(1, 11):
#     print(_)

# ## ইউজারের বয়স ইনপুট নিয়ে তাকে মেসেজ দেখাবে (যদি ১৮ এর বেশি হয়, তবে "You are an adult", নয়তো "You are not an adult")
# def student_age(age):
#     if age >=18:
#         print('You are an adult')
#     else:
#         print('You are not an adult')

# age = int(input('Enter your age'))
# student_age(age)

# ## ৩. একটি লিস্ট তৈরি করো, যেখানে পাঁচটি সংখ্যা থাকবে। তারপর সেই লিস্টের সব সংখ্যা প্রিন্ট করো এবং লিস্টের একটি সংখ্যা পরিবর্তন করে প্রিন্ট করো।
# my_list = [10, 14, 12, 34, 45]
# my_list[1] = 20
# print(my_list)

### dictionary
# student = {
#     'name' : 'rayhan',
#     'age' : 12,
#     'course' : 'python programming'
# }
# print(student['name'])

# ### new key value add in dictionary
# student['grade'] = 'A'
# print(student['grade'])

# ### দুটি সংখ্যার যোগফল বের করার জন্য একটি lambda ফাংশন
# add = lambda  x, y : x + y
# print(add(5,7))

# double = lambda x : x * 2
# print(double(5))

# num = [1,2,3,4,5,6,7,8,9,10]
# # doubled = [x * 2 for x in num]
# # print(doubled)

# even_nums = [x for x in num if x % 2 == 0]
# print(even_nums)

# ## 1. dictionary
# myself = {
#     'name' : 'rayhan',
#     'age' : 10,
#     'program' : 'python programming'
# }
# print(myself)

# ## 2. lambda function
# new_nums = lambda x, y, z : x + y + z
# print(new_nums(5,10,20))

# ## 3. list comprehention for odd nums
# nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# odd_nums = [x for x in nums if x % 2 != 0]
# print(odd_nums)

# students = {
#     'rayhan' : 20,
#     'roni' : 30,
#     'sabbir' : 40,
#     'pranto' : 50
# }
# for name, number in students.items():
#     print(f'{name} score {number}')

# cities = {
#     'dhaka' : 25,
#     'khulna' : 30,
#     'borishal' : 32,
#     'sylet' : 33,
#     'vola' : 24,
# }
# hotest_city = max(cities, key = cities.get)
# print(hotest_city)



# all_nums = lambda x , y : x + y

# print(all_nums(int(input('Enter Your Num1:')),int(input('Enter Your Num1:'))))


################# ‍SET ########################
# my_set = {12,15,11,13,18,16,19,17,20}
# my_set.add(6)
# my_set.remove(11)
# print(my_set)

# print(12 in my_set)

################# ‍TUPLE ########################
# my_tuple = (1,2,3,4,5,6,7,8,9)


# print(my_tuple)
# print(my_tuple[6])
# print(len(my_tuple))

# f = open('new.txt','r')
# # print(f.read())
# print(f.readline())  
# f.close()

# f = open('new.txt','w')
# f.write('\nrayhan')
# f.close()
# f = open('new.txt', 'r')
# print(f.read())
# f.close()

# f = open('new2.txt', 'x')
# f.close()
################################ append not work
################################ not work
# import os
# os.remove('new2.txt')

# # Step 1: ফাইল তৈরি ও লেখা
# with open('new.txt', 'w') as file:
#     # print(file.read())
#     file.write('Hello World!')

# # Step 2: ফাইল থেকে ডেটা পড়া
# with open('new.txt','r') as file:
#     print(file.read())

# # Step 3: ফাইলের শেষে নতুন ডেটা যোগ করা
# with open('new.txt', 'a') as file:
#     file.write('\nami rayhan')

# # Step 4: আবার ফাইল থেকে ডেটা পড়া
# with open('new.txt', 'r') as file:
#     print(file.read())


############### CSV #####################
import csv
# Step 1: নতুন একটি ফাইল তৈরি ও তাতে ডেটা লেখা
with open('contacts.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['name', 'phone', 'email'])
    writer.writerow(['rayhan', '0123456789', 'omuk@gmail.com'])
    writer.writerow(['pranto', '0123456789', 'pranto@gmail.com'])

# Step 2: ফাইল থেকে ডেটা পড়া
with open('contacts.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

