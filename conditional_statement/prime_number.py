# num = int(input("enter a number : "))  #5

# count = 0 
# for i in range(1, num+1):
#     if num % i == 0:
#         count = count + 1

# if count == 2:
#     print("num is prime")
# else:
#     print("number is not prime") 



 
num1 = int(input("enter 1st number : "))
num2 = int(input("enter 2nd number : "))
num3 = int(input("enter 3rd number : "))

if num1 > num2:
    if num1 > num3:
        print("num1 is greatest")
    else:
        print("num3 is greatest")
elif num2 > num3:
    print("num2 is greatest")
else:
    print("num3 is greatest")