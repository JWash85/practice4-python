#Python function called max_num() to find max 3 numbers
number= [30,50,5,6,1,100]
def max_num(x):
    max=0
    for i in x:
        if i>max:
            max=i
            print(max)
max_num(number)

#Python function called mult_list() to multiply all the numbers list

def mult_list(x):
    times=1
    for i in x:
        times *= i #Multiplying through the index[i] of the number list
    return times
print(mult_list(number))

'''
def mult_list(*args):
    times=1
    for i in args:
        times *= i
        print(times)
print(mult_list([30,50,5,6,1,100]))
'''

#Python function called rev_string() to reverse a string

def rev_string(*arg):
    number.reverse()
    return arg
print(rev_string(number))

#Python function called num_within() to check whether a number falls in a given range

def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,2,4))  #Does 3 fall between 2 - 5((a, b+1) or (2, 4+1)) returned boolean 
print(num_within(3,1,3))  # " "
print(num_within(10,2,5)) # " "
# output true, true, false
'''
def num_within(x):
    for i in x:
        if i in range(5, 100):
            return x
print(num_within(number))
'''
'''
def num_within(x):
    for i in range(len(x)):
        print(x[i])
num_within(number)
'''
#Python function called pascal() prints out the first n rows of pascal's triangle

def pascal(numRows):
  '''Print Pascal's triangle with numRows.'''
  for i in range(numRows):
    print(' '*(numRows-i), end='')
    # compute power of 11
    print(' '.join(str(11**i)))
pascal(1)
'''
output:
1
'''
pascal(5)
'''
output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''                                                             