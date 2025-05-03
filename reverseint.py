# def reverse_integer_arithmetic(n):
#     rev = 0
#     sign = -1 if n < 0 else 1
#     n = abs(n)

#     while n != 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n //= 10  # Integer division

#     return sign * rev

# # User input
# num = int(input("Enter an integer: "))
# print("Reversed integer:", reverse_integer_arithmetic(num))

def reverse_integer(num):
    reversed= 0 
    sign =-1 if num<0 else 1 
    num=abs(num)
    
    while num!=0:
        digit =num%10
        reversed=reversed *10 +digit
        num =num//10
        
    return sign * reversed
    
num =int(input("enter an integer:"))
print("reveresed integer" , reverse_integer(num))
        