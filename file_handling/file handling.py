
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

