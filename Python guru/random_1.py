'''
def calculate_area(length, width):
    return length*width
length =2
width = 4
print(calculate_area(length,width))


#chek if number is odd or even
def check_odd_even(list):
    list = [1,2,3,4,5,6,7,8,9,10]
    for i in list:
        if i%2 == 0:
            print(i = "Even")
        else:
            print(i = "Odd")

            

#reversing a string
def reverse_string(a):
    a = (["1", "2", "3", "4"])
    a.reverse(reverse = True)
    print(a)
    '''
     
#calculate_factorial
def calculate_factorial(i):
     
     if i < 0:
        print("Factorial is not defined for negative numbers!")
     elif i == 0:
        return 1
     else: 
          return i * calculate_factorial(i - 1)
     
i = int(input("Enter a positive integer: "))
print("Factorial of", i, "is", calculate_factorial(i))

'''
def calculate_factorial(i):
    if i < 0:
        print("Factorial is not defined for non-positive numbers!")
    elif i == 0:
        return 1
    else: 
        return i* calculate_factorial(i - 1)

i = int(input("Enter a positive integer: "))
print("Factorial of", i, "is", calculate_factorial(i))'''
