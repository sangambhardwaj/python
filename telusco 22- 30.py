# class 22
#     break, continue, pass


# x = int(input("how many candies you want"))
#
# i = 1
# while i <= x:
#     print("candy")
#     i = i + 1 # or used i +=1


# av = 5
#
# x = int(input("how many candies you want"))
#
# i = 1
# while i <= x:
#
#     if i > av:
#
#         print("out of the stock")
#
#         break #  used for out of the loop.
#     print("candy")
#
#     i = i + 1  # or used i +=1
#
# print("bye")


# for i in range(1,101):
#
#     if i%3==0 or i%5==0: # also used and function
#         continue
#
#     print(i)

#
#
# for i in range(1,101):
#
#     if i%2!=0:
#         pass
#
#     else:
#         print(i)
# print("bye")
#
#
# class 22.1
#     practice
#
# for i in range(5):
#     if i == 3:
#         continue
#     print("hello ", i)
#
#
# for i in range(5):
#     if i == 3:
#         break
#     print("hello ", i)
#
#
# def fun():
#     pass
#
#
#
# class 23
#     PRINTHING PATTERN IN PYTHON


# for i in range(4):
#     for j in range(4):
#
#         print("# ",end="")
#     print()
# #
# n = 1
#
#
#
#
# for i in range(4):
#     for j in range(i + 1):
#
#         print("#",end="")
#     print()
#
# for i in range(4):
#     for j in range(4-i):
#
#         print("#",end="")
#     print()
#
#
# class 24
#     for and else together

# nums = [12,16,18,21,25]
#
# for num in nums:
#     if num % 5 == 0:
#         print(num)
#
#
# nums = [12,16,18,20,25]
#
# for num in nums:
#     if num % 5 == 0:
#         print(num)
#         break
#
#
# nums = [10,16,18,20,25]
#
# for num in nums:
#     if num % 5 == 0:
#         print(num)
#         break
#
#
# nums = [12,16,18,22,23]
#
# for num in nums:
#     if num % 5 == 0:
#         print(num)
#         break
# else:
#     print("not found")
#
#
# class 25
#     PRIME NUMBER

# num = 10
#
# for i in range(2,num):
#     if num % i == 0:
#         print("not prime")
#         break
# else:
#     print("prime")
#
# def is_prime(number):
#     if number <= 1:
#         return False
#     for i in range(2, int(number**0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
#
# # Example usage:
# num = 10
# if is_prime(num):
#     print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")
#
#
# class 26
#     array









