'''
#print all evem numbers from range 1 to 20 using for loop
for i in range(2, 20):
    if i%2 == 0:
         print(i)
else:
    print()

#this is a shorter way to do it
for num in range(2, 21, 2):
    print(num)

'''

#sum of squares of numbers 1 to 10
sum_of_squares = 0
for i in range(1,11):
    print(i**2)
    sum_of_squares += i **2
print(sum_of_squares)
