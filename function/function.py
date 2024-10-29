# def student():
#     print("What's your name? ")
#     name = input()
#     print("Welcome " + name + " sPlease take your seat")

# for _ in range(100):
#     student()

# for i in range(5):
#     for _ in range(5):
#         print("*",end="")
#     print("")

# for i in range(1,5):
#     print("Enter first loop " + str(i))
#     for j in range(1,5):
#         print(f"Second loop working {j}")


### Number of levels in the pyramid
# n = 5
# Loop to create the pyramid
# for i in range(1, n+1):
#     # Print spaces to center-align the stars
#     print(' ' * (n-i), end='')
    
#     # Print stars
#     print('*' * (2*i-1))



### Number of levels in the pyramid
# n = 5

# # Loop to create the left half pyramid
# for i in range(1, n+1):
#     # Print stars for each row
#     print('*' * i)



### Number of levels in the pyramid
# n = 5

# # Loop to create the right half pyramid
# for i in range(1, n+1):
#     # Print spaces first to align the stars to the right
#     print(' ' * (n-i), end='')
    
#     # Print stars for each row
#     print('*' * i)