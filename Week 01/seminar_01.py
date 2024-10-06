import numpy as np

# basic examples on variables and print
x = 5 
x += 1
#print("Hello World")
#print(x * 10)

# ---------------- basic examples on data structures
# notice that the list is not bounded by type
example_list = [1, 2, '3', 'four'] 
example_set = set([1, 2, '3', 'four'])
example_dictionary = {'1' : 'one', '2' :'two', '3' : 'three'}\

# example of list of list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
three = list_of_lists[0][2]
#print(three)
four = list_of_lists[1][0]
#print(four)

# --------------- generating lists

# generates the numbers from 0 to 10 in my_list
my_list = [i for i in range(10)] 
#print(my_list)

# ** means i to the power of 2
# generates all squares of the numbers between 0 and 10
my_list2 = [i**2 for i in range(10)]
#print(my_list2)

# initialize 2d list 
list_2d = [[i + j for i in range(5)] for j in range(10)]

random_list = [3, 12, 5, 6]
sorted_list = sorted(random_list)
#print(sorted_list)

random_list = [(3, 'A'), (12, 'D'), (5, 'M'), (5, 'B')]
# sort the random_list by the second attribute
sorted_list = sorted(random_list, key = lambda x: x[1]) 
# print(random_list)
# print(sorted_list)

# ------------------- functions, loops, control flow

def myFunction(a, b):
    for num1 in range(a):
        if num1 % 2 == 0 and num1 % 4 == 0:
            print(str(num1) + " is multiple of four!")
        elif num1 % 2 == 0 and num1 % 4 != 0:
            print(str(num1) + " is even, but not a multiple of four!")
        else: 
            print(str(num1) + " is odd!")
    for num2 in range(1, b, 2):
        print(num2, 2**num2)

def main():
    a = 5
    b = 9
    myFunction(a, b)

# uncomment to call the main function
#main()

# ------------------ clases
class Vehicle:

    # constructor
    def __init__(self, make, name, year, is_electric=False, price=100):
        self.name = name
        self.make = make
        self.year = year
        self.is_electric = is_electric
        self.price = price

        self.odometer = 0

    def drive(self, distance):
        self.odometer += distance

    def compute_price(self):
        if self.odometer == 0:
            price = self.price
        elif self.is_electric:
            price = self.price / (self.odometer * 0.8)
        else:
            price = self.price / self.odometer
        return price

# if __name__ == '__main__':
#     family_car = Vehicle('Honda', 'Accord', '2019', price=10000)

#     print(family_car.compute_price())
#     family_car.drive(100)
#     print(family_car.compute_price())


# --------------------- numpy !!!
ones = np.ones(10)
#print(ones)
randomMatrix = np.random.rand(2, 3)
#print(randomMatrix)
x = np.array([1, 0, 0, 1])
y = np.array([-1, 5, 10, -1])
#print(x + y)


A = np.array([[5,10],[3,4]])
B = np.array([[6,20],[-4,-5]])
#print(A*B)

x = np.array([1,2,3,4])
y = np.array([5,10,15,20])
# 1*5 + 2*10 + 3*15 + 4*20
#print(np.dot(x,y))
# OUTPUT = 150 

res = sum([i * j for (i,j) in zip(x,y)])
#print(res)
# OUTPUT = 150

A = np.array([[1,10],[2,5],[3,3]])
x = np.array([3,4])
# 1*3 + 10*4 = 43
# 2*3 + 5*4 = 26
# 3*3 + 3*4 = 21
res1 = np.dot(A,x)
#print(res1)
# OUTPUT = [43 26 21]

A = np.array([[1,5],[2,3],[3,10]])
B = np.array([[3,4],[4,5]])
res2 = np.dot(A,B)
# OUTPUT = 
#[[23 29]
# [18 23]
# [49 62]]
res3 = np.matmul(A,B)
#print(res3)
# OUTPUT = 
#[[23 29]
# [18 23]
# [49 62]]


x = np.array([1,10,15,100])
#print(x+10)
# OUTPUT = [ 11  20  25 110]

A = np.array([[1,10],[15,20],[25,50]])
x = np.array([5,100])
A = A.shape
x = x.shape
print(A + x)