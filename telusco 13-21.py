# # # class 12
# # # NUMBER
# # # swap 2
# #
# # a = 5
# # b = 6
# # temp = a
# # a = b
# # b = temp
# # print(a)
# # print(b)
# #
# # # we also do same with other medhod
# #
# # a = 5 # 101 ( 3 bit)
# # b = 6 #110 (3 bit)
# # a = a+b # 11 #( 4 bit) 1 extra
# # b = a-b # 5
# # a = a-b # 6
# # print(a)
# # print(b)
# #
# # a = 5
# # b = 6
# # a = a ^ b  # (for save 1 extra bit use this medhod)
# # b = a ^ b
# # a = a ^ b
# # print(a)
# # print(b)
# #
# # a = 5
# # b = 6
# # a,b = b,a # (swaps the two top most stack item)
# # print(a)
# # print(b)
# #
# #
# # # class 14
# # #IDEL previous command
# # i don't know
# #
# # # class 15
# # # bitwise operations
# #
# # complement operator (~) or tilde operator # means ~n = n - 1
# # and(&) # both are same binary number
# # or(|) # if one is correct then true
# # XOR(^) # when both the binary numbers are different then get 1 otherwise 0
# # ^ = cap
# # left shift(<<) #  m << n  so adding n bits in m binary numbers
# # right shift(>>) #  m >> n so lossing n bits in m binary numbers
#
# print(~12) # add -12-1
# print(~1)
# print(bin(-13))
# print(~-45) # +45-1
#
# a = 12 & 13
# print(a)
# print(12 | 13)
# print(25 & 30)
# print(12 ^ 13)
# print(25 ^ 30)
# print(10 << 2)
# print(12 << 3)
# print(bin(12))
# print(0b110000)
# print(0b011110)
# print(bin(96))
# print(2 << 2)
# print(10 >> 2)
#
#
# class 16
# math functions
#
#
# import math
# x = math.sqrt(25)
# print(x)
# x = math.sqrt(15)
# print(x)
# print(math.floor(2.9)) # floor gives least value
# print(math.ceil(2.2)) # ceil gives higher value
# print(math.pow(3,4)) # use for power function
# print(math.pi)
# print(math.e)
#
# import math as mm
#
# print(math.sqrt(25))
# print(mm.sqrt(25))
#
# from math import sqrt,pow
#
# print(pow(3,5))
# print(sqrt(55))
# x = 5
# y = 6
# z = x + y
# print(z)

# class 18
#  use inputs in python

# x = input("enter 1st number")
# a = int(x)
# y = input("enter 2nd number")
# b = int(y)
# z = a + b
# print(z)
#
#  # other method
#
# x = int(input("enter 1st number "))
# y = int(input("enter 2nd number"))
# z = x + y
# print(z)

# ch = input('enter a char')[2]
# print(ch)
#
# ch = input('enter a char')
# print(ch[2])

# result = eval(input("enter an expr")) # evel fuction use for calcution
# print(result)


#  smjh nahi aya
#
# import sys
# x = int(sys.argv[1])
# y = int(sys.argv[2])
# z = x + y
# print(z)

#class 19


# x = 7
# r = x % 2
# if r==0:
#     print('even')
#     if r==1:
#        print('odd')
#
# print('bye')

#
# x = 7
# r = x % 2
# if r==0:
#     print('even')
#     if x>5: # this if is nested if
#         print('great')
#     else:
#         print("not so great")
# else:
#     print('odd')
#
# print('bye')
#

# if elis else concept
# x = 5
#
# if (x==1):
#     print("one")
# if x==2:
#     print("two")
# if x==3:
#     print("three")
# if x==4:
#     print("four")
# else:
#     print("can not be determine")
#
#
#
#
# x = 8
# if (x == 1):
#     print("one")
# elif x == 2:
#     print("two")
# elif x == 3:
#     print("three")
#
# elif x == 4:
#     print("four")
# else:
#     print("wrong input")
#
#
#class 20
#while loop


# i = 1 # initialization
#
# while i <=5: # Condition
#     print("Raj")
#     i = i +1 # Increment/ decrement


#
# i = 1
#
# while i<=12:
#     print("sangam",i)
#     i = i+5
#
# i = 15
#
# while i>=1:
#     print("sangam ji",i)
#     i = i-1 # decrement
#
#
# i = 1
#
# while i<=15:
#     print(i," sangam ji amra")
#     i = i+1 # decrement

# m = 1
# n = 1
# while m <= 2:
#     print(" section",m)
#
#     m = m + 1
#     while n <= 7:
#          print(" question",n)
#          n = n + 1
#          w = 1
#
#          while w <= 4:
#              print( w," option")
#              w = w + 1


#     i = 1
#     print()
#
# while i<=15:
#     print(i," sangam ji amra ",end="")
#     j = 1
#     while j <= 1:
#         print(" Rocks",end="")
#         j = j + 1
#     i = i + 1
#     print()


# class 21
#     for loop

# x = ['raj',125,2.5]
# m = 1
# while m <= 3:
#     for i in x:
#         print(m, i)
#         m = m + 1
#         print()
#
#
# x = ('sangam')
# for i in x:
#     print(i)

for i in range(11,21,1):
    print(i)

for i in range(20,11,-1):
    print(i)



for i in range(1,21):
    if i%5!=0: # != means not equal to
        print(i)