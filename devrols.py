def palindrome(num):
    num1 = 0
    num2 = num
    while num > 0:
        num1 = (num1*10) + num % 10
        num = num//10
    if num2 == num1:
        return True
    return False



num = 121
print(palindrome(num))

