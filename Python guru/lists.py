'''
def sum_of_lists(a, b, c):
    return a+b+c
def printsum(a,b,c):
    print(a+b+c)
print(sum_of_lists(1,2,3))

def sum_of_list(lst):
    total=0
    for num in lst:      #do more research into this see what should work
        total += num
        return total
    lst = [1, 2, 3, 4, 5]
    print(sum_of_list(lst))
'''
#return the max number
def find_max (list):
    list = [1,2,3,10,23]
    for i in list:
        print(max(i))
    else:
        print()